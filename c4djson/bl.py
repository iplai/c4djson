from typing import Union
import c4d, enum

__all__ = [
    "BL", "O", "T", "X", "F", "FL", "CT", "VP", "M", "Doc"
]


class Type(enum.Enum):
    """This is a Fake definition.
    Use pylance to color the node as Enum Member in vscode.
    ```
    "editor.semanticTokenColorCustomizations": {
        "enabled": true,
        "rules": {
            "enumMember": "#bae02d",
        }
    }
    ```
    """


from c4djson.bltype import Type


class BL:
    """A BaseList2D Node"""
    raws: dict[int, c4d.BaseList2D] = {}

    def __init__(self, type: Type):
        self.type = type
        self.obj: Union[c4d.BaseList2D, c4d.BaseObject] = c4d.BaseList2D(type.value)
        self.raw = BL.GetRaw(type.value)

    def __repr__(self):
        if self.obj.GetName() == self.raw.GetName():
            return str(self.type)
        return f"{self.type} @ '{self.obj.GetName()}'"

    def __matmul__(self, name: str):
        self.obj.SetName(name)
        return self

    def SetParent(self, parent: "BL"):
        if isinstance(self.obj, c4d.BaseObject):
            assert isinstance(parent.obj, c4d.BaseObject)
            self.obj.InsertUnderLast(parent.obj)
        if isinstance(self.obj, c4d.BaseTag):
            assert isinstance(parent.obj, c4d.BaseObject)
            parent.obj.InsertTag(self.obj, pred=parent.obj.GetLastTag())
        if isinstance(self.obj, c4d.BaseShader):
            parent.obj.InsertShader(self.obj)
        if isinstance(self.obj, c4d.CTrack):
            if self.type.value != c4d.CTbase:
                # Special track.
                tid = self.type.value
                self.obj = c4d.CTrack(parent.obj, c4d.DescID(tid, tid, 0))
                parent.obj.InsertTrackSorted(self.obj)
        if isinstance(self.obj, c4d.modules.mograph.FieldLayer):
            self.obj.InsertUnderLast(parent.obj)

    @property
    def link(self):
        return self.type.value, self.obj.GetName()

    @property
    def name(self):
        return self.obj.GetName()

    @classmethod
    def GetRaw(cls, tid: int):
        if tid not in cls.raws:
            try:
                cls.raws[tid] = c4d.BaseList2D(tid)
            except BaseException:
                return None
        return cls.raws[tid]

    @classmethod
    def FromObj(cls, obj: c4d.BaseList2D):
        blType: Type = Type.find(obj.GetType())
        if blType is None:
            return None
        try:
            bl = cls(blType)
        except BaseException:
            return None
        bl.obj = obj
        return bl


class O(Type):
    array = 5150
    atomarray = 1001002
    attractor = 5119
    background = 5122
    base = 5155
    basedeform = 5157
    baseeffector = 1018560
    basemogen = 1018639
    bend = 5128
    bevel = 431000028
    bezier = 5120
    bodycapture = 1053360
    bone_ex = 5123
    boole = 1010865
    bulge = 5129
    cacameraspacedeform = 1024476
    cacluster = 1021283
    cacollision = 1024544
    cacomponent = 1022292
    cacorrection = 1024542
    cajiggle = 1021284
    camera = 5103
    camesh = 1024543
    camorph = 1019768
    camuscle = 1026224
    capointcache = 1021318
    capsule = 5171
    caskin = 1026352
    casmooth = 1024529
    casquash = 1021280
    castep = 1026918
    casurface = 1024552
    character = 1021433
    cloth = 100004007
    cmotion = 1021824
    cone = 5162
    connector = 1011010
    connectorconstraint = 180000011
    cube = 5159
    cylinder = 5170
    datacapture = 1056362
    deflector = 5110
    destructor = 5124
    disc = 5164
    displacer = 1018685
    doodle = 1022242
    environment = 5106
    explosion = 5145
    explosionfx = 1002603
    extrude = 5116
    facecapture = 1040464
    falloff = 440000229
    feathers = 1018396
    ffd = 5108
    field = 440000200
    fieldremapper = 440000289
    figure = 5166
    floor = 5104
    force = 180000103
    foreground = 5121
    formula = 5146
    fractal = 5169
    friction = 5114
    fur = 1018958
    gravitation = 5111
    guide = 1027657
    instance = 5126
    joint = 1019362
    lathe = 5117
    layer = c4d.Olayer
    light = 5102
    line = 5137
    lod = 431000174
    loft = 5107
    melt = 5147
    metaball = 5125
    mgcloner = 1018544
    mgcoffee = 440000051
    mgdelay = 1019234
    mgeffectortarget = 1018889
    mgextrude = 1019358
    mgformula = 1018883
    mgfracture = 1018791
    mginheritance = 1018775
    mginstance = 1018957
    mgmatrix = 1018545
    mgplain = 1021337
    mgpolyfx = 1019222
    mgpushapart = 440000219
    mgpython = 1025800
    mgrandom = 1018643
    mgreeffector = 440000234
    mgroup = 1019351
    mgshader = 1018561
    mgsound = 440000255
    mgspline = 1018774
    mgsplinemask = 1019396
    mgsplinewrap = 1019221
    mgstep = 1018881
    mgtext = 1019268
    mgtime = 1018935
    mgtracer = 1018655
    mgvolume = 1021287
    mgvoronoifracture = 1036557
    mospline = 440000054
    motionclip = 465003002
    motiontracker = 1028393
    motor = 180000012
    null = 5140
    objecttracker = 1036100
    oiltank = 5172
    particle = 5109
    particlemodifier = 5158
    pivot = 100004839
    pivotmanipulator = 431000170
    plane = 5168
    planemanipulator = 431000167
    platonic = 5161
    plugin = 5154
    pluginpolygon = 1001091
    point = 5156
    polygon = 5100
    polyreduction = 1001253
    polyreduxgenerator = 465002101
    pyramid = 5167
    python = c4d.Opython
    relief = 5173
    remesh = 1054750
    rotation = 5112
    rsbakeset = 1040211
    rsenvironment = 1036757
    rsproxy = 1038649
    rssky = 1036754
    rsvolume = 1038655
    scatterobject = 1055907
    scatterplacement = 2000
    sds = 1007455
    selection = 5190
    shatter = 5148
    shear = 5131
    showdisplacement = 1001196
    shrinkwrap = 1019774
    simulationscene = 1057221
    singlepoly = 5174
    skin = 1019363
    sky = 5105
    sphere = 5160
    spherify = 1001003
    spline = 5101
    spline4side = 5180
    splinearc = 5182
    splinecircle = 5181
    splinecissoid = 5183
    splinecogwheel = 5188
    splinecontour = 5189
    splinecycloid = 5184
    splinedeformer = 1008982
    splineflower = 5176
    splineformula = 5177
    splinehelix = 5185
    splinenside = 5179
    splineprimitive = 5152
    splineprofile = 5175
    splinerail = 1008796
    splinerectangle = 5186
    splinestar = 5187
    splinetext = 5178
    spring = 180000010
    stage = 5136
    sweep = 5118
    symmetry = 5142
    taper = 5133
    torus = 5163
    tube = 5165
    turbulence = 5115
    twist = 5134
    vectorimport = 1057899
    volume = 1039858
    volumebuilder = 1039859
    volumecachelayer = 1050456
    volumefilter = 1039862
    volumeloader = 1039866
    volumemesher = 1039861
    volumeset = 1039867
    voronoipointgenerator = 1036448
    wave = 5135
    weighteffector = 1019677
    wind = 5113
    winddeform = 5149
    workplane = 5153
    wrap = 5143
    xref = 1025766
    xrefsimple = 200000118


class T(Type):
    alembicmorphtag = 1037184
    aligntopath = 5700
    aligntospline = 5699
    annotation = 1030659
    archigrass = 1028463
    bakeparticle = 5685
    baketexture = 1011198
    base = 5694
    cacheproxytag = 1050449
    cacheproxytagedgeselection = 1051632
    cacheproxytagpointselection = 1051631
    cacheproxytagpolyselection = 1051630
    cacomponent = 1022113
    caconstraint = 1019364
    caik = 1019561
    caikspline = 1019862
    cameracalibrator = 1026818
    cameraorrientation = 1029911
    capointcache = 1021302
    catension = 1018327
    cavisualselector = 1026275
    chardefinition = 1054858
    charmotiontransfer = 1055068
    cloth = 100004020
    clothbelt = 100004022
    collider = 100004021
    compositing = 5637
    connector = 1058895
    corner = 5712
    crane = 1028270
    display = 5613
    doodleimage = 1022211
    driver = 1019744
    dynamicsbody = 180000102
    edgeselection = 5701
    expresso = 1001149
    grouppriority = 200000299
    interaction = 440000164
    line = 5680
    lookatcamera = 1001001
    maskconstraint = 1029912
    meshattribute = 431000188
    metaball = 5684
    mgcolor = 1018768
    mgdependence = 1019352
    mgselection = 1021338
    mgtracer = 1019326
    mgweight = 440000231
    morphcam = 1027743
    motionblur = 5636
    motioncam = 1027742
    motionsystem = 465003000
    moveseye = 1040866
    movesposemorph = 1040839
    normal = 5711
    particle = 5630
    phong = 5612
    planarconstraint = 1029910
    plugin = 5691
    point = 5600
    pointselection = 5674
    polygon = 5604
    polygonselection = 5673
    posemorph = 1024237
    positionconstraint = 1029908
    protection = 5629
    python = 1022749
    render = 1018385
    restriction = 5683
    retarget = 100001735
    rope = 1018068
    ropebelt = 1018074
    rscamera = 1036760
    rsobject = 1036222
    savetemp = 5650
    scenenodes = 180420300
    sculpt = 1023800
    sds = 1007579
    sdsdata = 1018016
    segment = 5672
    sketchrender = 1011961
    sketchstyle = 1011012
    softselection = 1016641
    splinenormal = 440000173
    sticktexture = 5690
    stop = 5693
    sunexpression = 5678
    tangent = 5617
    targetexpression = 5676
    texture = 5616
    todo = 465001537
    userdata = 1041349
    uvw = 5671
    variable = 5695
    vectorconstraint = 1029909
    vertexcolor = 431000045
    vertexmap = 5682
    vibrate = 5698
    weights = 1019365


class X(Type):
    ambientocclusion = 1001191
    art = 1012161
    base = 5707
    bitmap = 5833
    brick = 5804
    cel = 1012158
    chanlum = 1007539
    checkerboard = 5800
    cloud = 5802
    color = 5832
    colorizer = 1011112
    colorstripes = 5822
    cyclone = 5821
    distorter = 1011114
    earth = 5825
    falloff = 1011101
    filter = 1011128
    fire = 5803
    flame = 5817
    formula = 1031433
    fresnel = 1011103
    fusion = 1011109
    galaxy = 5813
    gradient = 1011100
    hatch = 1012166
    layer = 1011123
    lensdistortion = 1031708
    lumas = 1011105
    marble = 5830
    metal = 5827
    mgbeat = 1018654
    mgcamera = 440000050
    mgcolor = 1018767
    mgmultishader = 1019397
    mosaic = 1022119
    movesface = 1040942
    noise = 1011116
    normaldirection = 1011107
    normalizer = 1026588
    objectcolor = 1033961
    pavement = 1024945
    planet = 5829
    polygonhair = 1017667
    posterizer = 1011111
    projector = 1011115
    proximal = 1011106
    rainsampler = 1026576
    ripple = 1011199
    rust = 5828
    simplenoise = 5807
    simpleturbulence = 5806
    spectral = 5831
    spline = 1011124
    spots = 1012160
    sss = 1001197
    star = 5816
    starfield = 5808
    sunburst = 5820
    terrainmask = 1026277
    thinfilm = 1035731
    tiles = 1011102
    translucency = 1011108
    variation = 1033825
    venus = 5826
    vertexmap = 1011137
    water = 5818
    wood = 5823
    xmbsubsurface = 1025614


class F(Type):
    box = 440000267
    capsule = 440000274
    cone = 440000269
    cylinder = 440000268
    formula = 440000280
    group = 1040449
    linear = 440000266
    python = 440000277
    radial = 1040448
    random = 440000281
    shader = 440000282
    sound = 440000283
    spherical = 440000243
    torus = 440000272


class FL(Type):
    base = 440000249
    clamp = 440000295
    colorize = 440000301
    curve = 440000297
    decay = 440000292
    delay = 440000291
    descid = 440000253
    field = 440000251
    folder = 440000250
    formula = 1040450
    gradient = 440000298
    invert = 440000300
    mograph = 440000325
    noise = 440000290
    particleobject = 440000330
    plugin = 440000259
    polygonobject = 440000327
    proximity = 1040379
    python = 1040420
    quantize = 440000299
    rangemap = 440000302
    remap = 440000296
    solid = 440000252
    spline = 440000276
    step = 440000293
    time = 1040451
    volumeobject = 440000328
    weight = 440000294


class CT(Type):
    base = c4d.CTbase
    ct2d = 1029916
    doodle = 1022213
    mask = 1029915
    morph = 100004822
    pla = 100004812
    sound = 100004813
    time = -1


class VP(Type):
    ambientocclusion = 300001045
    birender = 1028868
    bloom = 1040365
    colorcorrection = 1001008
    colormapping = 1001194
    comic = 1001009
    cylindricallens = 1001186
    demowatermark = 1037739
    globalillumination = 1021096
    gpurenderer = 1037639
    hlensdistortion = 1031709
    lenseffects = 1001049
    magicbulletlooks = 1054755
    medianfilter = 1001014
    normalpass = 1028398
    objectglow = 1001007
    opticsuite_depthoffield = 1001400
    opticsuite_glow = 1001401
    opticsuite_highlights = 1001402
    positionpass = 1027117
    remote = 1001015
    rsposteffects = 1040189
    rsrenderer = 1036219
    scenemotionblur = 1001010
    sharpenfilter = 1001013
    softfilter = 1001012
    tonemapping = 1037876
    toons = 1011015
    vectormotionblur = 1002008
    watermark = 1025462
    xmbsampler = 1023342


class M(Type):
    banji = 1011118
    banzi = 1011119
    base = 5702
    cgfx = 450000237
    cheen = 1011120
    danel = 1011117
    fog = 8803
    mabel = 1011121
    material = 5703
    nukei = 1011122
    outline = 1012041
    plugin = 5705
    pyroobject = 1001005
    pyrovolume = 1001006
    rsgraph = 1036224
    shadowcatcher = 1036101
    sketch = 1011014
    terrain = 8808


class Doc(Type):
    base = c4d.Tbasedocument


if __name__ == "__main__":
    import importlib, c4djson.bl
    importlib.reload(c4djson.bl)
