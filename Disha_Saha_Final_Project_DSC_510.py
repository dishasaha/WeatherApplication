'''

File: Disha_Saha_Final_Project_DSC_510.py
Name: Disha Saha
Date: 08/10/19
Course: DSC 510-T301
Assignment #: 10.2 Final Project
For your class project we will be creating an application that interacts with a webservice in order to obtain data.
Your program will use all of the information you’ve learned in the class in order to create a useful application.
Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
Your program must display the weather information in a READABLE format to the user.

'''

import json
import requests

#assigning the variables to construct the URL
Disha_key = "efefddc8ebe51d5c6b27e46abbc3ad94"
unitsformat='&units=imperial'
url = "http://api.openweathermap.org/data/2.5/weather?"

def retrieveWeatherByZip(zipcode): #function request the zip url and then getting a json
    try:
        get_url = url + "appid=" + Disha_key + "&zip=" + zipcode + unitsformat
        response = requests.get(get_url).json()
        return response
    except:
        print('Error retrieving data!')


def retrieveWeatherByCity(city): #function request the zip url and then getting a json
    try:
        get_url = url + "appid=" + Disha_key + "&q=" + city + unitsformat
        response = requests.get(get_url).json()
        return response
    except:
        print('Error retrieving data!')


def parseWeather(response):
    w_main = response['main'] #pulling out the dictionary of 'main
    #get returns the corressponding value in the dictionary and then print using .formart
    print('Current Temperature: {} degrees'.format((w_main.get('temp'))))
    print('Current Pressure:    {}hPa'.format(w_main.get('pressure')))
    print('Current Humidity:    {}%'.format(w_main.get('humidity')))
    print('Current Low Temp:    {} degrees'.format(w_main.get('temp_min')))
    print('Current High Temp:   {} degrees'.format(w_main.get('temp_max')))

def main():
    #welcome message to greet the user!
    print('Welcome to your one and only Weather App, where you can search by Zip Code or City anywhere in the US!\n')

    while (True): #the main loop that runs the show!

        try: #using try and except to forsee any errors
            question=int(input('Would you like to lookup weather data by City or zip code? '
                       'Enter 1 for Zip or 2 for City: \n'))
            if question==1: #conditional for zip code
                zip = input("Please enter the zip code :  ")
                answer=retrieveWeatherByZip(zip) #calling the retrieveweatherbyzip function
            elif question==2: #conditional for city
                city = input("Please enter the name of the City :  ")
                answer=retrieveWeatherByCity(city) #calling the retrieveweatherbycity function
            parseWeather(answer)  #calling the parseweather function


            additional=input('\nWould you like to continue Y/N: ') #check to see if the user still wants to go on
            check=additional.upper() #turn the input to uppercase to mitigate errors

            if check =='N':
                print('Thank you for checking the weather today! Goodbye!') #goodbye message
                break #ends program
            elif check =='Y' :
                continue  #conitnues from start

            else :  #trying to forsee any errors
                print('Error invalid input!')
                continue

        except: #if try fails to run this happens due to invalid entry
            print('Error! Please enter a valid input.')


#calling main the proper way
if __name__ == '__main__':
    main()



