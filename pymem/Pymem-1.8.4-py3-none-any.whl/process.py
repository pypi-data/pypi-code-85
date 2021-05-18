import ctypes
import locale
import logging
import os

import pymem.ressources.advapi32
import pymem.ressources.kernel32
import pymem.ressources.psapi
import pymem.ressources.structure


logger = logging.getLogger(__name__)


def get_python_dll(version):
    """"Given a python dll version will find its path using the current process as a placeholder

        Parameters
        ----------
        version: str
            A string representation of python version as a dll (python38.dll)

        Returns
        -------
        str
            The full path of dll
    """
    current_process_id = ctypes.c_void_p(os.getpid())
    current_process_handle = pymem.process.open(current_process_id)
    for module in pymem.process.enum_process_module(current_process_handle):
        if module.name == version:
            return module.filename


def inject_dll(handle, filepath):
    """Inject a dll into opened process.

        Parameters
        ----------
        handle: HANDLE
            Handle to an open object
        filepath: bytes
            Dll to be injected filepath

        Returns
        -------
        DWORD
            The address of injected dll
    """
    filepath_address = pymem.ressources.kernel32.VirtualAllocEx(
        handle,
        0,
        len(filepath),
        pymem.ressources.structure.MEMORY_STATE.MEM_COMMIT.value | pymem.ressources.structure.MEMORY_STATE.MEM_RESERVE.value,
        pymem.ressources.structure.MEMORY_PROTECTION.PAGE_EXECUTE_READWRITE.value
    )
    pymem.ressources.kernel32.WriteProcessMemory(handle, filepath_address, filepath, len(filepath), None)
    kernel32_handle = pymem.ressources.kernel32.GetModuleHandleW("kernel32.dll")
    load_library_a_address = pymem.ressources.kernel32.GetProcAddress(kernel32_handle, b"LoadLibraryA")
    thread_h = pymem.ressources.kernel32.CreateRemoteThread(
        handle, None, 0, load_library_a_address, filepath_address, 0, None
    )
    pymem.ressources.kernel32.WaitForSingleObject(thread_h, -1)
    pymem.ressources.kernel32.VirtualFreeEx(
        handle, filepath_address, len(filepath), pymem.ressources.structure.MEMORY_STATE.MEM_RELEASE.value
    )
    dll_name = os.path.basename(filepath)
    dll_name = dll_name.decode('ascii')
    module_address = pymem.ressources.kernel32.GetModuleHandleW(dll_name)
    return module_address


def get_luid(name):
    """
    Get the LUID for the SeCreateSymbolicLinkPrivilege
    """
    luid = pymem.ressources.structure.LUID()
    res = pymem.ressources.advapi32.LookupPrivilegeValue(None, name, luid)
    if not res > 0:
        raise RuntimeError("Couldn't lookup privilege value")
    return luid


def get_process_token():
    """
    Get the current process token
    """
    token = ctypes.c_void_p()
    res = pymem.ressources.advapi32.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), pymem.ressources.structure.TOKEN.TOKEN_ALL_ACCESS, token)
    if not res > 0:
        raise RuntimeError("Couldn't get process token")
    return token


def set_debug_privilege(lpszPrivilege, bEnablePrivilege):
    """Leverage current process privileges.

    :param lpszPrivilege: privilege name
    :param bEnablePrivilege: Enable privilege
    :type lpszPrivilege: str
    :type bEnablePrivilege: bool
    :return: True if privileges have been leveraged.
    :rtype: bool
    """
    # create a space in memory for a TOKEN_PRIVILEGES structure
    #  with one element
    size = ctypes.sizeof(pymem.ressources.structure.TOKEN_PRIVILEGES)
    size += ctypes.sizeof(pymem.ressources.structure.LUID_AND_ATTRIBUTES)
    buffer = ctypes.create_string_buffer(size)

    tp = ctypes.cast(buffer, ctypes.POINTER(pymem.ressources.structure.TOKEN_PRIVILEGES)).contents
    tp.count = 1
    tp.get_array()[0].LUID = get_luid(lpszPrivilege)
    tp.get_array()[0].Attributes = (
        pymem.ressources.structure.SE_TOKEN_PRIVILEGE.SE_PRIVILEGE_ENABLED if bEnablePrivilege else 0
    )
    token = get_process_token()
    res = pymem.ressources.advapi32.AdjustTokenPrivileges(token, False, tp, 0, None, None)
    if res == 0:
        raise RuntimeError("AdjustTokenPrivileges error: 0x%08x\n" % ctypes.GetLastError())

    ERROR_NOT_ALL_ASSIGNED = 1300
    return ctypes.windll.kernel32.GetLastError() != ERROR_NOT_ALL_ASSIGNED


def base_module(handle):
    """Returns process base address, looking at its modules.

    :param handle: A valid handle to an open object.
    :type handle: ctypes.c_void_p
    :param process_id: The identifier of the process.
    :type process_id: ctypes.c_void_p
    :return: The base address of the current process.
    :rtype: ctypes.c_void_p
    """
    hModules  = (ctypes.c_void_p * 1024)()
    process_module_success = pymem.ressources.psapi.EnumProcessModulesEx(
        handle,
        ctypes.byref(hModules),
        ctypes.sizeof(hModules),
        ctypes.byref(ctypes.c_ulong()),
        pymem.ressources.structure.EnumProcessModuleEX.LIST_MODULES_ALL
    )
    if not process_module_success:
        return # xxx
    module_info = pymem.ressources.structure.MODULEINFO(handle)
    pymem.ressources.psapi.GetModuleInformation(
        handle,
        ctypes.c_void_p(hModules[0]),
        ctypes.byref(module_info),
        ctypes.sizeof(module_info)
    )
    return module_info


def open(process_id, debug=None, process_access=None):
    """Open a process given its process_id.
    By default the process is opened with full access and in debug mode.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684320%28v=vs.85%29.aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa379588%28v=vs.85%29.aspx

    :param process_id: The identifier of the process to be opened
    :param debug: open process in debug mode
    :param process_access: desired access level
    :type process_id: ctypes.c_void_p
    :type debug: bool
    :type process_access: pymem.ressources.structure

    :return: A handle of the given process_id
    :rtype: ctypes.c_void_p
    """
    if debug is None:
        debug = True
    if not process_access:
        process_access = pymem.ressources.structure.PROCESS.PROCESS_ALL_ACCESS.value
    if debug:
        set_debug_privilege('SeDebugPrivilege', True)
    process_handle = pymem.ressources.kernel32.OpenProcess(process_access, False, process_id)
    return process_handle


def open_main_thread(process_id):
    """List given process threads and return a handle to first created one.

    :param process_id: The identifier of the process
    :type process_id: ctypes.c_void_p

    :return: A handle to the first thread of the given process_id
    :rtype: ctypes.c_void_p
    """
    threads = enum_process_thread(process_id)
    threads = sorted(threads, key=lambda t32: t32.creation_time)

    if not threads:
        return  # todo: raise exception

    main_thread = threads[0]
    thread_handle = open_thread(main_thread.th32ThreadID)
    return thread_handle


def open_thread(thread_id, thread_access=None):
    """Opens an existing thread object.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684335%28v=vs.85%29.aspx

    :param thread_id: The identifier of the thread to be opened.
    :type thread_id: ctypes.c_void_p

    :return: A handle to the first thread of the given process_id
    :rtype: ctypes.c_void_p
    """
    #XXX
    if not thread_access:
        thread_access = THREAD_ALL = 0x001F03FF
    thread_handle =  pymem.ressources.kernel32.OpenThread(thread_access, 0, thread_id)
    return thread_handle


def close_handle(handle):
    """Closes an open object handle.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211%28v=vs.85%29.aspx

    :param handle: A valid handle to an open object.
    :type handle: ctypes.c_void_p

    :return: If the function succeeds, the return value is nonzero.
    :rtype: bool
    """
    if not handle:
        return
    success = pymem.ressources.kernel32.CloseHandle(handle)
    return success


def list_processes():
    """List all processes

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms682489%28v=vs.85%29.aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684834%28v=vs.85%29.aspx

    :return: a list of process entry 32.
    :rtype: list(pymem.ressources.structure.ProcessEntry32)
    """
    SNAPPROCESS = 0x00000002
    hSnap = pymem.ressources.kernel32.CreateToolhelp32Snapshot(SNAPPROCESS, 0)
    process_entry = pymem.ressources.structure.ProcessEntry32()
    process_entry.dwSize = ctypes.sizeof(process_entry)
    p32 = pymem.ressources.kernel32.Process32First(hSnap, ctypes.byref(process_entry))
    if p32:
        yield process_entry
    while p32:
        yield process_entry
        p32 = pymem.ressources.kernel32.Process32Next(hSnap, ctypes.byref(process_entry))
    pymem.ressources.kernel32.CloseHandle(hSnap)


def process_from_name(name):
    """Open a process given its name.

    :param name: The name of the process to be opened
    :type name: str

    :return: The ProcessEntry32 structure of the given process.
    :rtype: ctypes.c_void_p
    """
    name = name.lower()
    processes = list_processes()
    for process in processes:
        if name in process.szExeFile.decode(locale.getpreferredencoding()).lower():
            return process


def process_from_id(process_id):
    """Open a process given its name.

    :param process_id: The identifier of the process
    :type process_id: ctypes.c_void_p

    :return: The ProcessEntry32 structure of the given process.
    :rtype: ctypes.c_void_p
    """
    processes = list_processes()
    for process in processes:
        if process_id == process.th32ProcessID:
            return process


def module_from_name(process_handle, module_name):
    """Retrieve a module loaded by given process.

    ex:
        d3d9 = module_from_name(process_handle, 'd3d9')

    :param process_handle: A process handle
    :param module_name: The module name
    :type process_handle: ctypes.c_void_p
    :type module_name: str
    :return: MODULEINFO
    """
    module_name = module_name.lower()
    modules = enum_process_module(process_handle)
    for module in modules:
        if module.name.lower() == module_name:
            return module


def enum_process_thread(process_id):
    """List all threads of given processes_id

    :param process_id: The identifier of the process
    :type process_id: ctypes.c_void_p

    :return: a list of thread entry 32.
    :rtype: list(pymem.ressources.structure.ThreadEntry32)
    """
    TH32CS_SNAPTHREAD = 0x00000004
    hSnap = pymem.ressources.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0)
    thread_entry = pymem.ressources.structure.ThreadEntry32()
    ret = pymem.ressources.kernel32.Thread32First(hSnap, ctypes.byref(thread_entry))

    if not ret:
        raise pymem.exception.PymemError('Could not get Thread32First')

    while ret:
        if thread_entry.th32OwnerProcessID == process_id:
            yield thread_entry
        ret = pymem.ressources.kernel32.Thread32Next(hSnap, ctypes.byref(thread_entry))
    pymem.ressources.kernel32.CloseHandle(hSnap)


def enum_process_module(handle):
    """List and retrieves the base names of the specified loaded module within a process

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms682633(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms683196(v=vs.85).aspx

    :param handle: A valid handle to an open object.
    :type handle: ctypes.c_void_p

    :return: a list of loaded modules
    :rtype: list(pymem.ressources.structure.MODULEINFO)
    """
    hModules  = (ctypes.c_void_p * 1024)()
    process_module_success = pymem.ressources.psapi.EnumProcessModulesEx(
        handle,
        ctypes.byref(hModules),
        ctypes.sizeof(hModules),
        ctypes.byref(ctypes.c_ulong()),
        pymem.ressources.structure.EnumProcessModuleEX.LIST_MODULES_ALL
    )
    if process_module_success:
        hModules = iter(m for m in hModules if m)
        for hModule in hModules:
            module_info = pymem.ressources.structure.MODULEINFO(handle)
            pymem.ressources.psapi.GetModuleInformation(
                handle,
                ctypes.c_void_p(hModule),
                ctypes.byref(module_info),
                ctypes.sizeof(module_info)
            )
            yield module_info


def is_64_bit(handle):
    """Determines whether the specified process is running under WOW64 (emulation).

    :param handle: A valid handle to an open object.
    :type handle: ctypes.c_void_p

    :return: True if the 32 bit process is running under WOW64.
    :rtype: bool
    """
    Wow64Process = ctypes.c_long()
    response = pymem.ressources.kernel32.IsWow64Process(handle, ctypes.byref(Wow64Process))
    return Wow64Process
