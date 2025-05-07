import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json

class CovidTracker:
    def __init__(self):
        self.base_url = "https://disease.sh/v3/covid-19"
        self.data = None

    def get_global_stats(self):
        """Fetch global COVID-19 statistics"""
        try:
            response = requests.get(f"{self.base_url}/all")
            if response.status_code == 200:
                self.data = response.json()
                return self.data
            else:
                print(f"Error fetching data: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def get_country_stats(self, country):
        """Fetch COVID-19 statistics for a specific country"""
        try:
            response = requests.get(f"{self.base_url}/countries/{country}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error fetching data for {country}: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def plot_global_stats(self):
        """Plot global COVID-19 statistics"""
        if not self.data:
            self.get_global_stats()
        
        if self.data:
            stats = {
                'Cases': self.data['cases'],
                'Deaths': self.data['deaths'],
                'Recovered': self.data['recovered']
            }
            
            plt.figure(figsize=(10, 6))
            plt.bar(stats.keys(), stats.values())
            plt.title('Global COVID-19 Statistics')
            plt.ylabel('Number of People')
            plt.xticks(rotation=45)
            
            # Add value labels on top of bars
            for i, v in enumerate(stats.values()):
                plt.text(i, v, f'{v:,}', ha='center', va='bottom')
            
            plt.tight_layout()
            plt.savefig('global_stats.png')
            plt.close()
            print("Global statistics plot saved as 'global_stats.png'")

def main():
    tracker = CovidTracker()
    
    while True:
        print("\nCOVID-19 Tracking System")
        print("1. Get Global Statistics")
        print("2. Get Country Statistics")
        print("3. Plot Global Statistics")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            stats = tracker.get_global_stats()
            if stats:
                print("\nGlobal COVID-19 Statistics:")
                print(f"Total Cases: {stats['cases']:,}")
                print(f"Total Deaths: {stats['deaths']:,}")
                print(f"Total Recovered: {stats['recovered']:,}")
                print(f"Active Cases: {stats['active']:,}")
        
        elif choice == '2':
            country = input("Enter country name: ")
            stats = tracker.get_country_stats(country)
            if stats:
                print(f"\nCOVID-19 Statistics for {country}:")
                print(f"Total Cases: {stats['cases']:,}")
                print(f"Total Deaths: {stats['deaths']:,}")
                print(f"Total Recovered: {stats['recovered']:,}")
                print(f"Active Cases: {stats['active']:,}")
        
        elif choice == '3':
            tracker.plot_global_stats()
        
        elif choice == '4':
            print("Thank you for using the COVID-19 Tracking System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 