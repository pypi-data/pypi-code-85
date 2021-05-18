from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class PlantGroOut(OutFile):
    """
    File reader for DSSAT plant growth (PLANTGRO.OUT) output files.
    """
    filename = 'PlantGro.OUT'

    def _get_var_info(self):
        return vars_

vars_ = {
    IntegerVar('TREATMENT', 2, info='Treatment number'),

    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    IntegerVar('DAP', 3, info='Days after planting'),
    FloatVar('L#SD', 4, 0, info='Leaf number'),
    FloatVar('GSTD', 4, 4, info='Growth stage'),
    FloatVar('LAID', 4, 2, info='Leaf Area Index'),
    IntegerVar('CWAD', 4, info='Tops dry weight, kg/Ha'),
    IntegerVar('VWAD', 4, info='Veg dry weight, kg/Ha'),
    IntegerVar('LWAD', 4, info='Leaf dry weight, kg/Ha'),
    IntegerVar('SWAD', 4, info='Stem dry weight, kg/Ha'),
    IntegerVar('FLWAD', 5, info='Flower dry weight, kg/Ha'),
    IntegerVar('FWAD', 4, info='Fruit dry weight, kg/Ha'),
    IntegerVar('CRAD', 4, info='Crown dry weight, kg/Ha'),
    IntegerVar('BWAD', 4, info='Basal dry weight, kg/Ha'),
    IntegerVar('SUGD', 4, info='Suck dry weight, kg/Ha'),
    IntegerVar('RWAD', 4, info='Root dry weight, kg/Ha'),
    FloatVar('HIAD', 4, 3, info='Harvest index'),
    IntegerVar('EYWAD', 5, info='Eye Weight, kg/Ha'),
    IntegerVar('EY#AD', 5, info='Eye number'),
    FloatVar('WSPD', 4, 3, info='Water stress in photosynthesis'),
    FloatVar('WSGD', 4, 3, info='Water stress in growth'),
    FloatVar('NSTD', 4, 3, info='Nitrogen stress'),
    FloatVar('LN%D', 4, 2, info='Leaf Nitrogen percentage'),
    FloatVar('SLAD', 4, 1, info='Specific Leaf area'),
    FloatVar('RDPD', 4, 1, info='Root depth, m'),
    FloatVar('RL1D', 4, 2, info='Level 1 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL2D', 4, 2, info='Level 2 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL3D', 4, 2, info='Level 3 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL4D', 4, 2, info='Level 4 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL5D', 4, 2, info='Level 5 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL6D', 4, 2, info='Level 6 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL7D', 4, 2, info='Level 7 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL8D', 4, 2, info='Level 8 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL9D', 4, 2, info='Level 9 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL10', 4, 2, info='Level 10 Root Length density, cm3/cm3 of soil'),

    # Recently added (#19)
    FloatVar('TMEAN', 5, 1, info='Mean Temperature (TMAX + TMIN/2, ºC'),
    FloatVar('PARID', 5, 3, info='PAR interception (%)'),
    FloatVar('PARUD', 5, 2, info='PAR utilization efficiency (g/MJ)'),
    FloatVar('AWAD', 4, 1, info='Assimilate Production (kg/(ha.d))'),
    FloatVar('SAID', 4, 3, info='Stem Area Index (m2/m2)'),
    FloatVar('CAID', 4, 4, info='Canopy Area Index'),
    IntegerVar('TWAD', 4, info='Tops + Roots + storage wt (kg[dm]/ha)'),
    IntegerVar('SDWAD', 5, info='Seed weight (kg/ha)'),
    IntegerVar('HWAD', 4, info='Harvest Product wt (kg [dm]/ha)'),
    IntegerVar('RSWAD', 5, info='Reserves weight (kg/ha)'),
    FloatVar('SNWLD', 5, 3, info='Senesced OM added to surface (kg/ha)'),
    FloatVar('SNWSD', 5, 4, info='Senesced OM added to soil (kg/ha)'),
    FloatVar('RS%D', 4, 2, info='Reserves Concentration (%)'),
    IntegerVar('S#AD', 4, info='Shoot (apex) Number (no/m2)'),
    FloatVar('SWXD', 4, 1, info='Extractable water (mm)'),
    FloatVar('WAVRD', 5, 1, info='Water available to demand ratio (#)'),
    FloatVar('WUPRD', 5, 2, info='Water uptake to demand ratio (#)'),
    FloatVar('WFPD', 4, 2, info='Water factor for photosynthesis (0-1)'),
    FloatVar('WFGD', 4, 2, info='Water factor for growth (0-1)'),
    FloatVar('NFPD', 4, 2, info='N factor for photosynthesis (0-1)'),
    FloatVar('NFGD', 4, 2, info='N factor for leaf growth (0-1)'),
    FloatVar('NUPRD', 5, 1, info='N uptake to demand ratio (#)'),
    FloatVar('TFPD', 4, 2, info='Temperature factor for photosyntesis (0-1)'),
    FloatVar('TFGD', 4, 2, info='Temperature factor for leaf growth (0-1)'),
    FloatVar('DYLFD', 5, 2, info='Daylength factor for development (0-1)'),

    IntegerVar('GWAD', 4, info='Grain dry weight (kg [dm]/ha)'),
    IntegerVar('G#AD', 4, info='Grain number (no/m2)'),
    FloatVar('GWGD', 4, 1, info='Unit grain weight (mg [dm]/grain'),
    IntegerVar('PWAD', 4, info='Pod weight (kg [dm]/ha)'),
    IntegerVar('P#AD', 4, info='Pod number (no/m2)'),
    FloatVar('EWSD', 4, 3, info='Excess water stress (0-1)'),
    FloatVar('PST1A', 5, 3, info='P stress factor for reducing photosynthate (0-1)'),
    FloatVar('PST2A', 5, 3, info='P stress factor which affects vegetative growth (0-1)'),
    FloatVar('KSTD', 4, 3, info='Potassium stress factor (0-1)'),
    FloatVar('SH%D', 4, 2, info='Shelling % (seed weight/pod wt * 100)'),
    FloatVar('HIPD', 4, 2, info='Pod harvest index (pod/top)'),
    IntegerVar('PWDD', 4, info='Detached pod mass (kg [dm]/ha)'),
    IntegerVar('PWTD', 4, info='Total pod weight (kg [dm]/ha)'),
    FloatVar('CHTD', 4, 2, info='Canopy height (m)'),
    FloatVar('CWID', 4, 2, info='Canopy width (m, for 1 row)'),
    FloatVar('RDPD', 4, 2, info='Root depth (m)'),
    IntegerVar('CDAD', 4, info='Dead canopy weight (kg [dm]/ha)'),
    IntegerVar('LDAD', 4, info='Dead leaf weight (kg [dm]/ha)'),
    IntegerVar('SDAD', 4, info='Dead stem weight (kg [dm]/ha)'), 
    IntegerVar('SNW0C', 5, info='Cumulative senesced dry matter to surface (kg/ha)'),
    IntegerVar('SNW1C', 5, info='Cumulative senesced dry matter to soil (kg/ha)'),
    FloatVar('DTTD', 4, 2, info='Growing degree days (ºC -d/d)'),
    FloatVar('NWAD', 4, 1, info='Nodule weight (kg [dm]/ha)'),
    FloatVar('TKILL', 4,1, info='Temperature for plant death (ºC)'),
    IntegerVar('CHWAD', 5, info='Chaff weight (kg/ha)'),
    IntegerVar('EWAD', 4, info='Ear (grain + chaff) or eye weight (kg [dm]/ha)'),
    IntegerVar('RSWAD', 5, info='Reserves weight (kg/ha)'),
    IntegerVar('SNWPD', 5, info='Dead material retained on plant (kg/ha)'),
    FloatVar('SNWLD', 5, 2, info='Senesced OM added to surface (kg/ha)'),
    FloatVar('SNWSD', 5, 4, info='Senesced OM added to soil (kg/ha)'),
    IntegerVar('H#AD', 4, info='Number (no/m2)'),
    FloatVar('HWUD', 4, 4, info='Harvest weight (wt/unit)'),
    IntegerVar('T#AD', 4, info='Tiller numer (no/m2)'),
    FloatVar('PTFD', 4, 2, info='Partition fraction of assimilates to shoot (0-1)'),
    FloatVar('WFTD', 4, 2, info='Water factor for transpiration (0-1)'),
    FloatVar('NFTD', 4, 2, info='N factor for tillering (0-1)'),
    FloatVar('VRNFD', 5, 2, info='Vernalization factor (0-1)')

}

