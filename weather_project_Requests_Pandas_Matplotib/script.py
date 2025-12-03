import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
# Calculate dates
today = datetime.now()

week_ago = today - timedelta(days=7)


start_date = week_ago.strftime("%Y-%m-%d") #strftime-> date time to string format i.e 2025-12-02
end_date = today.strftime("%Y-%m-%d")

weather_api_url = url = f"https://api.open-meteo.com/v1/forecast?latitude=27.717245&longitude=85.323959&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"


# get weather info


response= requests.get(weather_api_url)
data = response.json()
# print(data["daily"])

daily_data= data["daily"]


# create a data frame

df = pd.DataFrame({
    "date": daily_data["time"],
    "temp_max": daily_data["temperature_2m_max"],
    "temp_min": daily_data["temperature_2m_min"]
})

df["date"]= pd.to_datetime(df["date"])  #"2025-12-2" -> 2025-12-2
# print(df)

# save to csv
if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/kathmandu_weather.csv",index=False)
print("saved to csv")



plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temp_max'], marker='o', label='Max Temp')
plt.plot(df['date'], df['temp_min'], marker='o', label='Min Temp')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Kathmandu,Nepal Weather - Past 7 Days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('data/kathmandu_weather_chart.png')
plt.show()




