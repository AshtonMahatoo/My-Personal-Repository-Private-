#ifndef TIME_H
#define TIME_H

class Time
{
    private:
        int hour;
        int minute;
        int second;

    public:
        Time(const int h = 0, const int m = 0, const int s = 0); // Time with default values

        void setTime(const int h, const int m, const int s); // Setter Function

        void print()const; // Prints a description of object in "hh:mm:ss"

        bool equals(const Time&);
    
};
#endif