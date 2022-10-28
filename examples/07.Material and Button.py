from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.background: {
            T.texture: {
                c4d.TEXTURETAG_MATERIAL: M.material @ 'Background',
                c4d.TEXTURETAG_PROJECTION: c4d.TEXTURETAG_PROJECTION_FRONTAL,
            },
        },
        O.cube @ "Edges": {
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.MODE_OFF,
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.MODE_OFF,
            O.mgrandom: {
                c4d.ID_MG_BASEEFFECTOR_STRENGTH: 3.0,
                c4d.MGRANDOMEFFECTOR_MODE: c4d.MGRANDOMEFFECTOR_MODE_NOISE,
                c4d.MGRANDOMEFFECTOR_SPEED: 0.25,
                c4d.ID_MG_EFFECTORDEFORMER_MODE: c4d.ID_MG_EFFECTORDEFORMER_MODE_POINT,
            },
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.cube @ 'Edges',
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_EDGE,
            c4d.MG_POLYEDGE_SCALE_ACTIVE: True,
            c4d.MG_POLYEDGE_SCALE: 0.98,
            T.texture: {c4d.TEXTURETAG_MATERIAL: M.material @ 'Glass'},
            O.cylinder: {
                c4d.PRIM_CYLINDER_RADIUS: 8,
                c4d.PRIM_CYLINDER_HEIGHT: 100,
                c4d.PRIM_CYLINDER_HSUB: 8,
                c4d.PRIM_CYLINDER_FILLET: True,
                c4d.PRIM_CYLINDER_FSUB: 5,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                O.bulge: {
                    c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.MODE_OFF,
                    c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.MODE_OFF,
                    # c4d.DEFORMOBJECT_SIZE: (16.0, 100.0, 16.0),  # This is the result of the button click
                    c4d.DEFORMOBJECT_FITTOPARENT: True,            # This is a button!
                    c4d.DEFORMOBJECT_STRENGTH: -0.7,
                },
            },
        },
        M.material @ 'Background': {
            c4d.MATERIAL_USE_COLOR: False,
            c4d.MATERIAL_USE_LUMINANCE: True,
            c4d.MATERIAL_LUMINANCE_SHADER: X.gradient,
            X.gradient: {c4d.SLA_GRADIENT_TYPE: c4d.SLA_GRADIENT_TYPE_2D_CIRC},
        },
        M.material @ 'Glass': {
            c4d.MATERIAL_USE_COLOR: False,
            c4d.MATERIAL_USE_TRANSPARENCY: True,
        },
    })
    gradient_shader = tree[X.gradient]
    gradient: c4d.Gradient = gradient_shader[c4d.SLA_GRADIENT_GRADIENT]
    gradient.InvertKnots()
    gradient_shader[c4d.SLA_GRADIENT_GRADIENT] = gradient
    tree.load().print()
    Command.unfoldall()
    # Command.playforward()
