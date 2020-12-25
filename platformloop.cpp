#include <iostream>



using namespace std;

//
class PlatformSpace{
    private:
        int intBuffer;
    public:
        void setintBuffer(int newintBuffer){
            intBuffer = newintBuffer;
        }
        int getintBuffer(){
            return intBuffer;
        }
};


int main(){

    bool platformRunning = true;
    PlatformSpace platformSpace;

    platformSpace.setintBuffer(100);
    int countDracula = 0;

    do {
        countDracula = platformSpace.getintBuffer();
        countDracula--;
        platformSpace.setintBuffer(countDracula);
        cout << countDracula << endl;
        if(platformSpace.getintBuffer() < 0){
            platformRunning = false;
        }
    }
    
    while(platformRunning == true);

    return 0;
};