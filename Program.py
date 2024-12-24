from PIL import Image
import numpy as np
import math
from Errors import WrongExtensionError, OutOfRangeError
from Classes import Point, Line
from DataLoad import LoadImageWithArray, LoadParameters


def FindObstacle(image, line):
    image_array = np.array(image.convert("RGB"))
    height, width = image_array.shape[:2]
    for point in line.LinePoints():
        if 0 <= point.x < width and 0 <= point.y < height:
            neighbors = [
                (point.x - 1, point.y), (point.x + 1, point.y),
                (point.x, point.y - 1), (point.x, point.y + 1),
                (point.x - 1, point.y - 1), (point.x + 1, point.y + 1),
                (point.x - 1, point.y + 1), (point.x + 1, point.y - 1)
            ]
            for nx, ny in neighbors:
                if (image_array[ny, nx] == [0, 0, 0]).all():
                    return point
            if (image_array[point.y, point.x] == [0, 0, 0]).all():
                return point
    return None


def DrawLine(image_array, line_points, line_length=60):
    for point in line_points[:line_length]:
        image_array[point.y, point.x] = [255, 0, 0]


def FindLineEndingPoints(x1, y1, angle, length=60):
    angle = int(angle) % 360
    angle_rad = math.radians(angle)
    x2 = x1 + length * math.cos(angle_rad)
    y2 = y1 - length * math.sin(angle_rad)
    return Point(int(x2), int(y2))


def SimulateLaserScanner(image_path, params_path):
    image, image_array = LoadImageWithArray(image_path)
    start_point, base_angle = LoadParameters(params_path)
    line_lengths = []
    line_angles = [base_angle - 90 + 10 * i for i in range(19)]

    for angle in line_angles:
        end_point = FindLineEndingPoints(
            start_point.x, start_point.y, angle)
        line = Line(start_point, end_point)
        line_points = line.LinePoints()
        line_length = 0
        obstacle = FindObstacle(image, line)

        for point in line_points:
            if 0 <= point.x < 320 and 0 <= point.y < 240:
                if point == obstacle:
                    line_length += 1
                    break
                line_length += 1
            else:
                break
        line_lengths.append(line_length)
        DrawLine(image_array, line_points, line_length)

    return image_array, line_lengths


def main():
    environment_path = "otoczenie.png"
    params_path = "parametry.txt"

    try:
        print("Starting simulation")
        image_array, line_lengths = (
            SimulateLaserScanner(environment_path, params_path))

        simulation_image = Image.fromarray(image_array)
        simulation_image.save("symulacja.png")
        print("Simulation image saved as 'symulacja.png'")

        with open("wyniki.txt", "w") as file:
            file.write('\n'.join(map(str, line_lengths)))
        print("Line lengths saved to 'wyniki.txt'")

    except WrongExtensionError as e:
        print(f"Error: {e}")
    except OutOfRangeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
