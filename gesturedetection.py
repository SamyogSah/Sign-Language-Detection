    
   #####################################GESTURE DETECTION#################################
    
    
    #while True:
       # fps = cvFpsCalc.get()

        # Process Key (ESC: end) #################################################
       # key = cv.waitKey(10)
       # if key == 27:  # ESC
       #     break
       # number, mode = select_mode(key, mode)

        # Camera capture #####################################################
        #ret, image = cap.read()
       # if not ret:
       #     break
       # image = cv.flip(image, 1)  # Mirror display
       # debug_image = copy.deepcopy(image)

        # Detection implementation #############################################################
        #image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

       # image.flags.writeable = False
      #  results = hands.process(image)
       # image.flags.writeable = True

       # if mode == 2:
            # Loading image while processing the dataset
        #    loading_img = cv.imread("./assets/om606.png", cv.IMREAD_COLOR)

           # cv.putText(
           #     loading_img,
            #    "Loading...",
            ##    cv.FONT_HERSHEY_SIMPLEX,
             #   1.0,
             #   (255, 255, 255),
             #   4,
             #   cv.LINE_AA,
           # )

           # cv.imshow("Hand Gesture Recognition", loading_img)

          #  key = cv.waitKey(1000)

            # Looping through each folder of the dataset
          #  imglabel = -1
           # for imgclass in os.listdir(datasetdir):
           #     imglabel += 1
            #    numofimgs = 0
            #    for img in os.listdir(os.path.join(datasetdir, imgclass)):
             #       numofimgs += 1
             #       imgpath = os.path.join(datasetdir, imgclass, img)
              #      try:
             #          img = cv.imread(imgpath)
                    #    debug_img = copy.deepcopy(img)

                    #    for _ in [1, 2]:
                    #        img.flags.writeable = False
                         #   results = hands.process(img)
                         #   img.flags.writeable = True

                        #    if results.multi_hand_landmarks is not None:
                         #       for hand_landmarks, handedness in zip(
                         #           results.multi_hand_landmarks,
                         #           results.multi_handedness,
                        #        ):
                        #            # Bounding box calculation
                       #             brect = calc_bounding_rect(
                        #                debug_img, hand_landmarks
                       #             )
                         #           # Landmark calculation
                         #           landmark_list = calc_landmark_list(
                         #               debug_img, hand_landmarks
                         #           )
#
                                    # Conversion to relative coordinates / normalized coordinates
                          #          pre_processed_landmark_list = pre_process_landmark(
                         #               landmark_list
                        #            )

                                    # Write to the dataset file
                        #            logging_csv(
                        #                imglabel, mode, pre_processed_landmark_list
                        #            )
                       #     img = cv.flip(img, 0)
               #     except Exception as e:
               #         print(f"Issue with image {imgpath}")
#
            #    print(f"Num of image of the class {imglabel} is : {numofimgs}")
       #     mode = 1
        #    print("End of job!")
        #    break
       # else:
      #      if results.multi_hand_landmarks is not None:
#for hand_landmarks, handedness in zip(
           #         results.multi_hand_landmarks, results.multi_handedness
           #     ):
                    # Bounding box calculation
          #          brect = calc_bounding_rect(debug_image, hand_landmarks)
                    # Landmark calculation
            #        landmark_list = calc_landmark_list(debug_image, hand_landmarks)
#
                    # Conversion to relative coordinates / normalized coordinates
            #        pre_processed_landmark_list = pre_process_landmark(landmark_list)

                    # Write to the dataset file
              #      logging_csv(number, mode, pre_processed_landmark_list)

                    # Hand sign classification
                 #   hand_sign_id = keypoint_classifier(pre_processed_landmark_list)

                    # Finger gesture classification
                #    finger_gesture_id = 0

                    # Drawing part
                  #  debug_image = draw_bounding_rect(use_brect, debug_image, brect)
                 #   debug_image = draw_landmarks(debug_image, landmark_list)
                 #   debug_image = draw_info_text(
                  #      debug_image,
                  #      brect,
                  #      handedness,
                   #     keypoint_classifier_labels[hand_sign_id],
                 #   )

         #   debug_image = draw_info(debug_image, fps, mode, number)

            # Screen reflection #############################################################
        #    cv.imshow("Hand Gesture Recognition", debug_image)

 #   cap.release()
  #  cv.destroyAllWindows()
