import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
df=pd.read_csv("country_wise_latest.csv")
pd.DataFrame(df)
# print(df)
def indian_format(x, pos): #converting the in Indian digits
    if x >= 1e7:
        return f'{x*1.0/1e7:.1f} Cr'
    elif x >= 1e5:
        return f'{x*1.0/1e5:.1f} L'
    else:
        return f'{x:.0f}'


x=np.array(["Death","Recoverd","Confirmed"])
y=np.array([df["Deaths"].sum(),df["Recovered"].sum(),df["Confirmed"].sum()])
fig, ax = plt.subplots()
ax.bar(x,y,color="red",label="total patient")
ax.yaxis.set_major_formatter(FuncFormatter(indian_format))
plt.xlabel("Catagories")
plt.ylabel("Number of Patient ")
plt.title("Bar Graph showing the Deaths, Recovered and Confirmed in Covid 19")
plt.legend()
plt.tight_layout()
plt.savefig("PatientGrapt.png",dpi=300)
plt.show()
print(df["Country/Region"].count())

#shoowing the countries having higher deth  than 40000
filtercountry=df[df['Deaths']>40000]["Country/Region"].value_counts()
filterdeath40000=df[df["Deaths"]>40000]["Deaths"]
print(filtercountry)
plt.title("Showing the Countries having higher than 40,000 Deaths in Covid 19 ")
plt.pie(filterdeath40000,labels=filtercountry.index,autopct="%1.1f%%",colors=["Red","Green","Blue","Orange"])
plt.show()


# Total Confirmed vs Deaths vs Recovered
# Aggregate global totals
total_confirmed = df["Confirmed"].sum()
total_deaths = df["Deaths"].sum()
total_recovered = df["Recovered"].sum()
total_active = df["Active"].sum()

# Plot line chart (snapshot-style)
labels = ['Confirmed', 'Deaths', 'Recovered']
values = [total_confirmed, total_deaths, total_recovered]

fig,ax=plt.subplots(1,2)
ax[0].plot(labels, values, marker='o', linestyle='-', color='blue')
ax[0].set_title("Global COVID-19 Snapshot")
ax[0].set_xlabel("Status")
ax[0].set_ylabel("Total Cases")
ax[0].grid(True)

# ax[0].savefig("Covidsnapshot.png",dpi=300)



ax[1].scatter(labels, values, marker='o', linestyle='-', color='blue')
ax[1].set_title("Global COVID-19 Snapshot")
ax[1].set_xlabel("Status")
ax[1].set_ylabel("Total Cases")
ax[1].grid(True)

plt.savefig("lineplotVsScatterplot.png",dpi=300)
plt.show()



# Sort and select top 10 countries by confirmed cases
top_confirmed = df.sort_values(by="Confirmed", ascending=False).head(10)

# Sort and select top 10 countries by deaths
top_deaths = df.sort_values(by="Deaths", ascending=False).head(10)

# Create subplots
plt.figure(figsize=(14, 6))

# Bar chart for top 10 countries by confirmed cases
plt.subplot(1, 2, 1)
plt.barh(top_confirmed["Country/Region"], top_confirmed["Confirmed"], color='skyblue')
plt.xlabel("Total Confirmed Cases")
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.gca().invert_yaxis()  # To show the highest value at the top

# Bar chart for top 10 countries by deaths
plt.subplot(1, 2, 2)
plt.barh(top_deaths["Country/Region"], top_deaths["Deaths"], color='salmon')
plt.xlabel("Total Deaths")
plt.title("Top 10 Countries by COVID-19 Deaths")
plt.gca().invert_yaxis()

# Adjust layout
plt.tight_layout()
plt.savefig("Top10.png",dpi=300)
plt.show()

# PIE CHART: Distribution of countries per WHO region
region_counts = df["WHO Region"].value_counts()

# BAR CHART: Total confirmed cases per WHO region
region_confirmed = df.groupby("WHO Region")["Confirmed"].sum().sort_values(ascending=False)

# Create the plots
plt.figure(figsize=(14, 6))

# Pie chart: Number of countries in each WHO region
plt.subplot(1, 2, 1)
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Countries by WHO Region")

# Bar chart: Total confirmed cases per WHO region
plt.subplot(1, 2, 2)
plt.bar(region_confirmed.index, region_confirmed.values, color='mediumseagreen')
plt.xticks(rotation=45)
plt.ylabel("Total Confirmed Cases")
plt.title("Confirmed COVID-19 Cases by WHO Region")

# Final layout adjustments
plt.tight_layout()
plt.savefig("WHOandconfir.png",dpi=300)
plt.show()