import math

def euclidean_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    # Noktaları tanımla
    points = [(1, 2), (3, 4), (5, 6)]

    # Mesafeleri hesapla
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            distances.append(distance)

    # Minimum mesafeyi bulma ve yazdırma
    min_distance = min(distances)
    print("Minimum mesafe:", min_distance)

if __name__ == "__main__":
    main()

