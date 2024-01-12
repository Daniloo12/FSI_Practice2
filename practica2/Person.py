import cv2
import random


class Person:
    person_id = 0
    all_people = []

    # Constructor
    def __init__(self, center, x_coord, y_coord, width, height, color, template, last_frame):
        """
        - x_center (int): X coordinate of the center of the detection rectangle
        - y_center (int): Y coordinate of the center of the detection rectangle
        - x_coord (int): X coordinate of the rectangle
        - y_coord (int): Y coordinate of the rectangle
        - width (int): Width of the rectangle
        - height (int): Height of the rectangle
        """
        Person.person_id += 1
        self.person_id = Person.person_id
        self.center = center
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.color = color
        self.template = template
        self.last_frame = last_frame

    def get_center(self):
        return self.center

    def get_color(self):
        return self.color

    def set_center(self, new_center):
        self.center = new_center

    def set_x_coord(self, new_x_coord):
        self.center = new_x_coord

    def set_y_coord(self, new_y_coord):
        self.center = new_y_coord

    def set_template(self, new_template):
        self.center = new_template

    def set_width(self, new_width):
        self.center = new_width

    def set_height(self, new_height):
        self.center = new_height

    def update_coordinates(self, new_x_coord, new_y_coord, new_center, current_frame):
        self.x_coord = new_x_coord
        self.y_coord = new_y_coord
        self.center = new_center
        self.last_frame = current_frame

    @classmethod
    def create_person(cls, center, x, y, width, height, template, current_frame):
        color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        Person.all_people.append(Person(center, x, y, width, height, color, template, current_frame))
        return Person.all_people[-1].person_id

    @classmethod
    def same_person(cls, template, frame, center, x, y, current_frame):

        close_centers = []
        for person in Person.all_people:
            if (abs(person.center[0] - center[0]) < 3 and abs(person.center[1] - center[1]) < 25) or (
                    abs(person.x_coord - x) < 15 and abs(person.y_coord - y) < 55):
                close_centers.append(person)
            if (current_frame - person.last_frame) >= 20:
                Person.all_people.remove(person)

        if len(close_centers) == 0:
            return None

        if len(close_centers) == 1:
            close_centers[0].update_coordinates(x, y, center, current_frame)
            return close_centers[0]

        if 2 <= len(close_centers) <= 5:
            person_found = min(close_centers, key=lambda person: (abs(person.get_center()[1] - center[1])))
            person_found.update_coordinates(x, y, center, current_frame)
            return person_found

        else:
            for person in close_centers:
                x_start = person.x_coord - 40
                y_start = person.y_coord - 40
                if person.x_coord - 40 < 0:
                    x_start = 0
                if person.y_coord - 40 < 0:
                    y_start = 0
                roi = frame[y_start:person.y_coord + 100, x_start:person.x_coord + 100]
                cv2.imshow("ROI", roi)
                template_comparison = cv2.matchTemplate(roi, person.template, cv2.TM_SQDIFF_NORMED)
                min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(template_comparison)
                if max_value > 0.95:
                    person.template = template
                    person.update_coordinates(x, y, center)
                    return person