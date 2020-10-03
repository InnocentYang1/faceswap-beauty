# ----------shape predictor 68 face landmarks---------------------
# face key points
JAW_POINTS = list(range(0, 17))
RIGHT_BROW_POINTS = list(range(17, 22))
LEFT_BROW_POINTS = list(range(22, 27))
NOSE_POINTS = list(range(27, 36))
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))
MOUTH_OUT_POINTS = list(range(48, 60))
MOUTH_IN_POINTS = list(range(60, 68))
# select key points by myself
BROW_EYE_NOSE = RIGHT_BROW_POINTS + LEFT_BROW_POINTS + RIGHT_EYE_POINTS + LEFT_EYE_POINTS + \
                NOSE_POINTS
MOUTH_1 = list((49, 53, 55, 59, 48, 54))
MOUTH_2 = list((49, 53, 55, 59, 61, 63))
MOUTH_3 = list(range(49, 54)) + list(range(55, 60)) + list(range(61, 64)) + list(range(65, 68))
MOUTH_4 = list((49, 53, 55, 59))
MOUTH_ALL = MOUTH_OUT_POINTS + MOUTH_IN_POINTS
# ----------shape predictor 68 face landmarks---------------------

# ----------shape predictor 81 face landmarks---------------------
jaw_point = list(range(0, 17)) + list(range(68, 81))
right_brow = list(range(17, 22))
left_brow = list(range(22, 27))
nose = list(range(27, 36))
right_eye = list(range(36, 42))
left_eye = list(range(42, 48))
mouth = list(range(48, 60))
align = (left_brow + right_eye + left_eye +
         right_brow + nose + mouth)
# ----------shape predictor 81 face landmarks---------------------

WRAP_REGION = JAW_POINTS + BROW_EYE_NOSE
MASK_REGION = JAW_POINTS + RIGHT_BROW_POINTS + LEFT_BROW_POINTS

