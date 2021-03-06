

# = Positions and Vectors =====================================================
"""
Vector math, projection, and compositing. For use in 3D rendering and
navigation.
"""


# - Dependencies ---------------------------------
# Python Modules
import math
# Local Modules


# - Vector Math Functions ------------------------
def unit_vector(V):
    """Calculates a vector of magnitude 1 in the direction of vector V."""
    return scale_vector(V, 1/magnitude(V))


def vector_between(S, E):
    """Calculates the vector between S and E (start and end)."""
    return (E[0]-S[0], E[1]-S[1], E[2]-S[2])


def distance(S, E):
    """Calculates the distance between S and E (start and end)."""
    return math.sqrt((E[0]-S[0])**2 + (E[1]-S[1])**2 + (E[2]-S[2])**2)


def magnitude(V):
    """Calculates the magnitude of a given vector."""
    return math.sqrt(V[0]**2 + V[1]**2 + V[2]**2)


def vector_addition(A, B):
    """Calculates the sum of two vectors."""
    return (A[0]+B[0], A[1]+B[1], A[2]+B[2])


def scale_vector(V, scale):
    """Scales vector V by the scalar scale."""
    return (V[0]*scale, V[1]*scale, V[2]*scale)


def scalar_product(A, B):
    """Calculates the scalar product (dot product) of vectors A and B."""
    return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]


def vector_product(A, B):
    """Calculates the vector product (cross product) of vectors A and B."""
    return (A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0])


def scalar_projection(A, B):
    """Calculates the scalar projection of A onto B."""
    return scalar_product(A, B) / magnitude(B)


def vector_projection(A, B):
    """Calculates the vector projection of A onto B."""
    return scale_vector(
        unit_vector(A),
        scalar_projection(A, B),
    )


def transform_coordinate_system(position, viewpoint, axes):
    """Transforms point from one coordinate system into point in another."""
    delta_position = vector_between(viewpoint, position)
    return (
        scalar_product(delta_position, axes[0]),
        scalar_product(delta_position, axes[1]),
        scalar_product(delta_position, axes[2]),
    )
