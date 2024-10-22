#include <iostream>
#include <cmath>
#include <vector>
#include <memory>  // For smart pointers

using namespace std;

// Drone class to represent each drone's position, velocity, and radius
class Drone {
public:
    double x, y;    // Position ft - assume level flight. No altitude change.
    double vx, vy;  // Velocity kts
    double radius;  // Collision radius

    Drone(double x, double y, double vx, double vy, double radius)
        : x(x), y(y), vx(vx), vy(vy), radius(radius) {}

    // Update the drone's position based on its velocity
    void updatePosition() {
        x += vx;
        y += vy;
    }

    // Print the drone's current position and velocity
    void printStatus() const {
        cout << "Drone at (" << x << " ft, " << y << " ft), Velocity: (" << vx << ", " << vy << " kts)\n";
    }
};

// Function to calculate the distance between two drones
double distanceBetweenDrones(unique_ptr<Drone>& d1, unique_ptr<Drone>& d2) {
    return sqrt(pow(d2->x - d1->x, 2) + pow(d2->y - d1->y, 2));
}

// Function to adjust velocities to avoid collisions
void avoidCollision(unique_ptr<Drone>& d1, unique_ptr<Drone>& d2) {
    double dist = distanceBetweenDrones(d1, d2);
    double collisionDist = d1->radius + d2->radius;

    if (dist < collisionDist) {
        // Normalize the distance vector between drones
        double dx = d2->x - d1->x;
        double dy = d2->y - d1->y;
        double magnitude = sqrt(dx * dx + dy * dy);
        dx /= magnitude;
        dy /= magnitude;

        // Move the drones apart by adjusting their velocities
        d1->vx -= dx * 0.1;  // Move drone 1 away
        d1->vy -= dy * 0.1;
        d2->vx += dx * 0.1;  // Move drone 2 away
        d2->vy += dy * 0.1;
    }
}

// Simulate multiple drones and apply collision avoidance
int main() {
    // Allocate memory for drones using smart pointers
    vector<unique_ptr<Drone>> drones;

    drones.push_back(make_unique<Drone>(50, 50, 5, 5, 2));   // Drone 1
    drones.push_back(make_unique<Drone>(300, 300, -5, -5, 2)); // Drone 2
    drones.push_back(make_unique<Drone>(200, 200, -2, -2, 2)); // Drone 3
    
    //Debug initial state of all drones
    cout << "\n --- Input drone positions ---- \n";
    for (auto& drone : drones) {
            drone->printStatus();
    }


    // Simulate for 10 time steps
    for (int step = 0; step < 10; step++) {
        cout << "\nTime Step " << step << ":\n";
        //drone->printStatus();
        // Update positions and check for collisions
        for (size_t i = 0; i < drones.size(); i++) {
            for (size_t j = i + 1; j < drones.size(); j++) { 
                avoidCollision(drones[i], drones[j]);
            }
        }

        // Update all drones' positions
        for (auto& drone : drones) {
            drone->updatePosition();
            drone->printStatus();
        }
    }
    return 0;
}
