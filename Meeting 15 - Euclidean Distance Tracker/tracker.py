import math


class EuclideanDistTracker:

    def __init__(self):
        self.center_points = {}
        self.id_count = 0

    def update(self, objects_rect):

        objects_bbs_ids = []

        # find center point coordinates of each detected object
        for rect in objects_rect:

            x, y, width, height = rect
            cx = (x + x + width) // 2
            cy = (y + y + height) // 2
            # print(cx, cy)

            is_same_object = False

            for object_id, point in self.center_points.items():

                distance = math.hypot(cx - point[0], cy - point[1])

                # if distance lower than 50, assume objects are the same object
                if distance < 50:
                    self.center_points[object_id] = (cx, cy)
                    objects_bbs_ids.append([x, y, width, height, object_id])
                    is_same_object = True
                    break

            if not is_same_object:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, width, height, self.id_count])
                self.id_count += 1

            new_center_points = {}

            for obj_bb_id in objects_bbs_ids:
                Nx, Ny, Nw, Nh, object_id = obj_bb_id
                center = self.center_points[object_id]
                new_center_points[object_id] = center

            self.center_points = new_center_points.copy()

            print(self.center_points)
            return objects_bbs_ids

        return objects_bbs_ids
