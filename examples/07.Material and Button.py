from c4djson.core import *

doc.Flush()

if __name__ == "__main__":
    tree = Tree({
        O.background: {
            T.texture: {
                c4d.TEXTURETAG_MATERIAL: M.material @ 'Background',
                c4d.TEXTURETAG_PROJECTION: c4d.TEXTURETAG_PROJECTION_FRONTAL,
            },
        },
        O.cube @ 'Edges': {
            # Viewport Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            # Renderer Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            O.mgrandom: {
                c4d.ID_MG_BASEEFFECTOR_STRENGTH: 3,
                # Random Mode: Noise
                c4d.MGRANDOMEFFECTOR_MODE: c4d.MGRANDOMEFFECTOR_MODE_NOISE,
                # Animation Speed
                c4d.MGRANDOMEFFECTOR_SPEED: 0.25,
                # Deformation: Point
                c4d.ID_MG_EFFECTORDEFORMER_MODE: c4d.ID_MG_EFFECTORDEFORMER_MODE_POINT,
            },
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.cube @ 'Edges',
            # Distribution: Edge
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_EDGE,
            # Scale on Edge
            c4d.MG_POLYEDGE_SCALE_ACTIVE: True,
            # Edge Scale
            c4d.MG_POLYEDGE_SCALE: 0.98,
            T.texture: {c4d.TEXTURETAG_MATERIAL: M.material @ 'Glass'},
            O.cylinder: {
                c4d.PRIM_CYLINDER_RADIUS: 8,
                c4d.PRIM_CYLINDER_HEIGHT: 100,
                # Height Segments
                c4d.PRIM_CYLINDER_HSUB: 8,
                c4d.PRIM_CYLINDER_FILLET: True,
                # Fillet Segments
                c4d.PRIM_CYLINDER_FSUB: 5,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                O.bulge: {
                    # Viewport Visibility: Off
                    c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
                    # Renderer Visibility: Off
                    c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
                    c4d.DEFORMOBJECT_SIZE: (16, 100, 16),
                    c4d.DEFORMOBJECT_STRENGTH: -0.7,
                },
            },
        },
        M.material @ 'Background': {
            # Enable Color
            c4d.MATERIAL_USE_COLOR: False,
            # Enable Luminance
            c4d.MATERIAL_USE_LUMINANCE: True,
            # Texture
            c4d.MATERIAL_LUMINANCE_SHADER: X.gradient,
            X.gradient: {
                c4d.SLA_GRADIENT_GRADIENT: {
                    c4d.GRADIENT_KNOT: {
                        1: {
                            c4d.GRADIENTKNOT_COLOR: (255, 255, 255),
                            c4d.GRADIENTKNOT_BRIGHTNESS: 1.0,
                            c4d.GRADIENTKNOT_POSITION: 0.0,
                            c4d.GRADIENTKNOT_BIAS: 0.5,
                            c4d.GRADIENTKNOT_ID: 1,
                            c4d.GRADIENTKNOT_INTERPOLATION: c4d.GRADIENT_INTERPOLATION_SMOOTHKNOT,
                        },
                        2: {
                            c4d.GRADIENTKNOT_COLOR: (0, 0, 0),
                            c4d.GRADIENTKNOT_BRIGHTNESS: 1.0,
                            c4d.GRADIENTKNOT_POSITION: 1.0,
                            c4d.GRADIENTKNOT_BIAS: 0.5,
                            c4d.GRADIENTKNOT_ID: 2,
                            c4d.GRADIENTKNOT_INTERPOLATION: c4d.GRADIENT_INTERPOLATION_SMOOTHKNOT,
                        },
                    },
                    c4d.GRADIENT_MODE: c4d.GRADIENTMODE_COLOR,
                    c4d.GRADIENT_UNCLAMPED: False,
                },
                c4d.SLA_GRADIENT_TYPE: c4d.SLA_GRADIENT_TYPE_2D_CIRC,
            },
        },
        M.material @ 'Glass': {
            # Enable Color
            c4d.MATERIAL_USE_COLOR: False,
            # Enable Transparency
            c4d.MATERIAL_USE_TRANSPARENCY: True,
        },
    })
    tree.load()
