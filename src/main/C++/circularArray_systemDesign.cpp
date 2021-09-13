/*
Circular Array: Implement a CircularArray class that supports an array-like data structure which
can be efficiently rotated. If possible, the class should use a generic type (also called a template), and
should support iteration via the standard for (Obj o : circularArray) notation.
*/

#include<iostream>
#include<vector>

using namespace std;

template<class T>
class CircularArray{
    
    class Iterator{
        private:
            typename vector<T>::iterator begin;
            int ind;
            int size;
            int traversed;
            bool end = false;

        public:
            Iterator(vector<T>& vec, int ind,bool isEnd=false):ind(ind){
                begin = vec.begin();
                size = vec.size();
                traversed=0;
                end = isEnd;
            }

            //when used ++ should return the same object pointing to the next element.
            Iterator& operator ++(){
                ind = (ind+1)%size;
                traversed++;
                if(size==traversed){
                    end=true;
                }
                return *this;
            }

            //when dereferenced should return value of data[current]
            T operator*(){
                return *(begin+ind);
            }

            //or when iteration not finished != should give false.
            bool operator!=(const Iterator& other){
                if (end)
                    return false;
                
                return true;
            }


    };

    private:
        //data structure
        vector<T> data;
        int size;
        int startInd;
        int endInd;
        int nextInd;


    public:
        CircularArray(int size):size(size){
            data = vector<T>(size);
            startInd=0;
            endInd=size-1;
            nextInd=0;
        }
        void add(int e){
            data[nextInd]=e;
            nextInd = (nextInd+1) % size;
        }
        void rotate(int rightShift){
            startInd=(startInd + rightShift)%size;
            startInd=(startInd + rightShift)%size;
            endInd=(endInd + rightShift)%size;
        }

        T get(int index){
            if(index>size-1)
            {
                cout<<"Error on input"<<endl;
                return 0;
            }

            return data[(startInd+index)%size];
        }

        void print(){

            for(int i=0;i<size;i++){
                cout<<data[(startInd+i)%size]<<" ";
            }
            cout<<endl;
        }

        // should return an iterator object that points to data[start]
        auto begin(){
            return Iterator(data,startInd);
        }


        auto end(){
            return Iterator(data,startInd,true);
        }

};

int main(){

    CircularArray<int> cir_arr(6);

    cir_arr.add(1);
    cir_arr.add(2);
    cir_arr.add(3);
    cir_arr.add(4);
    cir_arr.add(5);
    cir_arr.add(6);

    cir_arr.print();
    cir_arr.rotate(2);
    cir_arr.print();



    CircularArray<char> cir_arr_char(4);

    cir_arr_char.add('a');
    cir_arr_char.add('b');
    cir_arr_char.add('c');
    cir_arr_char.add('d');
    cir_arr_char.print();
    cir_arr_char.rotate(1);
    cir_arr_char.print();



    
    for(auto e:cir_arr_char)
        cout<<e<<" ";



    return 0;
}