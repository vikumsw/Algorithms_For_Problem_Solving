/*
Design a parking lot
*/
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<memory>


using namespace std;

enum class Size {SMALL,MEDIUM,LARGE};

class Vehicle{
    private:
        Size size;
        string licensePlate;
    
    public:
        Vehicle(Size size,string licensePlate):size(size),licensePlate(licensePlate){};
        Size getSize(){return size;}
        string getLicensePlate(){return licensePlate;}
};

class MotorCycle: public Vehicle {
    // fits to any S,M,L spot
    public:
        MotorCycle(string licensePlate):Vehicle(Size::SMALL, licensePlate){};
};
    
class Car: public Vehicle{
    // fits to any M,L spot
    public:
        Car(string licensePlate):Vehicle(Size::MEDIUM, licensePlate){};
};
class Bus: public Vehicle{
    // fits only to a L spot
    public:
        Bus(string licensePlate):Vehicle(Size::LARGE, licensePlate){};
};

enum class Status {EMPTY,FULL};

class ParkingSpot{
    private:
        int slotID;
        int levelID;
        Size size;
        Status status = Status::EMPTY;
        shared_ptr<Vehicle> vehicle;

    public:
        ParkingSpot(int slotID,int levelID, Size size):slotID(slotID),levelID(levelID),size(size){}
        bool isAvaialable(){
            if (status==Status::EMPTY)
                return true;
            return false;
        }
        Size getSlotSize(){return size;}
        void addVehicle(shared_ptr<Vehicle> _vehicle){
            vehicle = _vehicle;
            status = Status::FULL;
            cout<<"Vehicle:"<< vehicle->getLicensePlate()<<" Added to Slot:["<<levelID<<","<<slotID<<"]"<<endl;
        }
        void removeVehicle(){
            string licencePlate = vehicle->getLicensePlate();
            shared_ptr<Vehicle> vehicle = nullptr;
            status = Status::EMPTY;
            cout<<"Vehicle:"<< licencePlate <<" Removed from Slot:["<<levelID<<","<<slotID<<"]"<<endl;
        }
};

class Level{
    private:
        bool isAvailable = true;
        int levelID;
        vector<shared_ptr<ParkingSpot>> parkingSpots;

    public:
        Level(int i):levelID(i){
            parkingSpots.push_back(make_shared<ParkingSpot>(1,i,Size::SMALL));
            parkingSpots.push_back(make_shared<ParkingSpot>(1,i,Size::MEDIUM));
            parkingSpots.push_back(make_shared<ParkingSpot>(1,i,Size::LARGE));
        }
        shared_ptr<ParkingSpot> getFreeSpot(Size size){
            for(auto spot:parkingSpots){
                if(spot->isAvaialable() && spot->getSlotSize()==size)
                    return spot;
            }
            return nullptr;
        }
        bool isSlotAvailable(Size size){
            for(auto spot:parkingSpots){
                if(spot->isAvaialable() && spot->getSlotSize()==size)
                    return true;
            }
            return false;
        }
        void freeSpot(ParkingSpot*){/*todo*/}
        void setAvaialbility(){/*todo*/}
        bool isAvaialble(){/*todo*/}

};

class ParkingLot{
    using licensePlate = string;
    private:
        vector<Level> levels;
        int availableSpots;
        map<licensePlate,shared_ptr<ParkingSpot>> parkedVehicles;
        int levelCount = 5;

    public:
        ParkingLot(){
            for(int i=0;i<levelCount;i++){
                levels.push_back(Level(i));
            }
        }

        void addVehicle(shared_ptr<Vehicle> vehicle){
            cout<<"Adding vehicle:"<< vehicle->getLicensePlate()<<" -> ";
            bool added = false;
            for(int i=0;i<levelCount;i++){
                if (levels[i].isSlotAvailable(vehicle->getSize())){
                    auto spot = levels[i].getFreeSpot(vehicle->getSize());
                    spot->addVehicle(vehicle);
                    parkedVehicles.insert(make_pair(vehicle->getLicensePlate(),spot));
                    added = true;
                    availableSpots--;
                    break;
                }
            }
            
            if(!added)
                cout<<"No Space for Vehicle"<< vehicle->getLicensePlate()<<endl;
        }
        void removeVehicle(string licencePlate){
            cout<<"Removing Vehicle:"<<licencePlate<<" -> ";

            //check for existence
            if (parkedVehicles.end() != parkedVehicles.find(licencePlate)){
                auto spot = parkedVehicles.find(licencePlate)->second;
                spot->removeVehicle();
            }
            else{
                cout<<"Vehicle not found:"<<licencePlate<<endl;
            }
        }
        int getAvailableSpots(){return availableSpots;}
};




int main(){
    cout<<"Starting Parking Lot Simulator"<<endl;

    ParkingLot carPark;
    carPark.addVehicle(make_shared<MotorCycle>("M123"));
    carPark.addVehicle(make_shared<MotorCycle>("M124"));
    carPark.addVehicle(make_shared<MotorCycle>("M125"));
    carPark.addVehicle(make_shared<MotorCycle>("M126"));
    carPark.addVehicle(make_shared<MotorCycle>("M127"));
    carPark.removeVehicle("M123");
    carPark.addVehicle(make_shared<MotorCycle>("M128"));

    carPark.removeVehicle("C890");
    


    return 0;
}