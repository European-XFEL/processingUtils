
def rotate_coordinates_on_ccd(x_in, y_in, rot, ccd_width, ccd_height):
    """
    Calculates the CCD coordinates of a point, in a rotated CCD
    coordinates system

    :param x_in: X coordinate of original point
    :param y_in: Y coordinate of original point
    :param rot: clockwise rotation of the CCD in degrees.
        Must be a multiple of 90 degrees.
    :param ccd_width: the width of the CCD
    :param ccd_height: the height of the CCD
    :return: the x,y coordinates of the rotated point
    """
    if rot % 90 != 0:
        raise ValueError("Rotation must a multiple of 90 degrees")

    rot_right_angles = (rot // 90) % 4

    if rot_right_angles == 0:
        x_out = x_in
        y_out = y_in
    elif rot_right_angles == 1:
        x_out = y_in
        y_out = ccd_width + 1 - x_in
    elif rot_right_angles == 2:
        x_out = ccd_width + 1 - x_in
        y_out = ccd_height + 1 - y_in
    elif rot_right_angles == 3:
        x_out = ccd_height + 1 - y_in
        y_out = x_in
    else:
        raise RuntimeError  # that's a bug
    return x_out, y_out


def rotate_roi(roi_topleft_x, roi_topleft_y, roi_width, roi_height, rot,
               ccd_width, ccd_height):
    """
    Define a ROI in a rotated CCD coordinates system

    :param roi_topleft_x: X coord. of input ROI top-left corner
    :param roi_topleft_y: Y coord. of input ROI top-left corner
    :param roi_width: width of input ROI top-left corner
    :param roi_height: height of input ROI top-left corner
    :param rot: clockwise rotation of the CCD in degrees.
        Must be a multiple o 90 degrees, from -270 to +270
    :param ccd_width: the width of the CCD
    :param ccd_height: the height of the CCD
    :return: topleft X, topleft Y, width and heigh of the ROI in the rotated
        coordinates system
    """
    roi_bottomright_x = roi_topleft_x + roi_width - 1
    roi_bottomright_y = roi_topleft_y + roi_height - 1

    x1, y1 = rotate_coordinates_on_ccd(roi_topleft_x, roi_topleft_y,
                                       rot, ccd_width, ccd_height)
    x2, y2 = rotate_coordinates_on_ccd(roi_bottomright_x, roi_bottomright_y,
                                       rot, ccd_width, ccd_height)

    roi_out_x = min(x1, x2)
    roi_out_y = min(y1, y2)
    roi_out_width = abs(x2 - x1) + 1
    roi_out_height = abs(y2 - y1) + 1
    return roi_out_x, roi_out_y, roi_out_width, roi_out_height
