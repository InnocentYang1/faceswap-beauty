#! /usr/bin/env python
import os
import cv2
import argparse

from face_detection import select_face
from face_swap import face_swap
from makeup import makeup_face
from beauty import beauty_face


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FaceSwapApp')
    parser.add_argument('--src', default='images\\users\\1.png', help='Path for source image')
    parser.add_argument('--dst', default='images\\templates\\1.jpg', help='Path for target image')
    parser.add_argument('--out', default='images\\outputs\\output.jpg', help='Path for storing output images')
    parser.add_argument('--makeup', default=True, action='store_true', help='2d or 3d warp')
    parser.add_argument('--correct_color', default=True, action='store_true', help='Correct color')
    parser.add_argument('--beauty', default=True, action='store_true', help='Don\'t show debug window')
    args = parser.parse_args()

    # Read images
    src_img = cv2.imread(args.src)
    dst_img = cv2.imread(args.dst)

    # makeup the src face
    if args.makeup:
        src_img = makeup_face(src_img)

    # Select src face
    src_points, src_shape, src_face = select_face(src_img)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        print('Detect 0 Face !!!')
        exit(-1)

    output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img, args.correct_color)

    # beauty the face
    if args.beauty:
        src_img = beauty_face(src_img)

    dir_path = os.path.dirname(args.out)

    cv2.imwrite(args.out, output)

    # --------------------------Test code begin-----------------------------
    # correct_color = True
    # face_makeup = True
    # face_beauty = True
    #
    # users = range(1, 9)
    # templates = range(1, 9)
    #
    # # for template in templates:
    # for user in users:
    #     for template in templates:
    #         user = str(user)
    #         template = str(template)
    #         src_path = 'images/users/' + user + '.png'
    #         dst_path = 'images/templates/' + template + '.jpg'
    #         out_path = 'images/final/' + template + '_' + user + '_no' + '.jpg'
    #         # out_path2 = 'images/final/' + user + '_' + user + '' + '.jpg'
    #
    #         # Read images
    #         src_img = cv2.imread(src_path)
    #         dst_img = cv2.imread(dst_path)
    #
    #         # makeup the src face
    #         if face_makeup:
    #             src_img = makeup_face(src_img)
    #             # dst_img = makeup_face(dst_img)
    #         # cv2.imwrite('images/makeup/t' + str(user) + '.jpg', src_img)
    #         # cv2.imwrite('images/makeup/u' + str(user) + '.jpg', dst_img)
    #
    #         # Select face
    #         src_points, src_shape, src_face = select_face(src_img)
    #         dst_points, dst_shape, dst_face = select_face(dst_img)
    #
    #         if src_points is None or dst_points is None:
    #             print('Detect 0 Face !!!')
    #             exit(-1)
    #
    #         # face_swap
    #         image = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img, correct_color)
    #
    #         # beauty the face
    #         if face_beauty:
    #             src_img = beauty_face(src_img)
    #         # cv2.imwrite(out_path2, src_img)
    #
    #         # save image
    #         cv2.imwrite(out_path, image)
    # --------------------------Test code end----------------------------
