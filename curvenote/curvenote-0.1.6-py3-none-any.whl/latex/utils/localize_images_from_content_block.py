from ...client import Session
from .regex import INLINE_IMAGE_BLOCK_REGEX
from .patch_local_images_from_tex_block import patch_local_images_from_tex_block
from .get_image_block import get_image_block


def localize_images_from_content_block(
    session: Session, assets_folder: str, content: str
):
    """Process image blocks and their respective referencing data including:
    - captions
    - labels
    """
    patch = patch_local_images_from_tex_block(INLINE_IMAGE_BLOCK_REGEX, content)
    content_with_extensions = patch.content

    for block_path, local_path in zip(patch.block_paths, patch.local_paths):
        # get block
        image_block, local_path_with_extension = get_image_block(
            session, assets_folder, block_path, local_path
        )

        # now patch the image captions which will be marked have placeholders like
        # f"{local_path}.caption"
        content_with_extensions = content_with_extensions.replace(
            f"{local_path}.caption", image_block.caption
        )

        # patch the remaining image block references
        content_with_extensions = content_with_extensions.replace(
            local_path, local_path_with_extension
        )

    return content_with_extensions
