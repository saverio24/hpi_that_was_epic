import matplotlib.pyplot as plt

def calculate_co2():
    """
    Calculate and display a user's estimated annual CO₂ footprint.

    This function collects lifestyle data from the user (transportation habits,
    electricity usage, and meat consumption), applies standard CO₂ emission
    factors, and computes annual emissions for each category. It prints the
    numerical results, provides simple feedback based on the user's total
    emissions, and generates a bar chart visualizing emissions by category.

    The function performs the following steps:
    1. Prompt the user for weekly or monthly activity data.
    2. Convert the input into annual CO₂ emissions using predefined emission factors.
    3. Organize results into a dictionary for display and plotting.
    4. Print detailed results and an overall yearly footprint.
    5. Display a bar chart using matplotlib to visualize emissions.

    No arguments are required, and no values are returned.
    All results are displayed directly to the user.
    """
    print("🌍 Personal CO₂ Footprint Calculator\n")

    # --- User input ---
    km_car = float(input("How many km do you drive by car per week? "))
    km_bus = float(input("How many km do you travel by bus per week? "))
    km_plane = float(input("How many km do you travel by plane per year? "))
    electricity_use = float(input("Monthly electricity consumption (kWh): "))
    meat_meals = int(input("How many meals with meat per week? "))

    # --- Emission factors (kg CO₂ per unit) ---
    CO2_CAR = 0.12       # per km
    CO2_BUS = 0.05       # per km
    CO2_PLANE = 0.25     # per km
    CO2_ELECTRICITY = 0.233  # per kWh
    CO2_MEAT = 5.0       # per meal

    # --- Annual calculations ---
    co2_car = km_car * 52 * CO2_CAR
    co2_bus = km_bus * 52 * CO2_BUS
    co2_plane = km_plane * CO2_PLANE
    co2_electricity = electricity_use * 12 * CO2_ELECTRICITY
    co2_food = meat_meals * 52 * CO2_MEAT

    total = co2_car + co2_bus + co2_plane + co2_electricity + co2_food

    # --- Data for the chart ---
    categories = {
        "Car": co2_car,
        "Bus": co2_bus,
        "Plane": co2_plane,
        "Electricity": co2_electricity,
        "Food (meat)": co2_food
    }

    # --- Text output ---
    print("\n📊 Estimated annual CO₂ emissions:")
    for cat, val in categories.items():
        print(f" - {cat}: {val:.1f} kg CO₂")
    print(f"\n🌱 Total annual footprint: {total:.1f} kg CO₂")

    # --- Simple feedback ---
    if total > 10000:
        print("⚠️ Above average emissions. Try reducing car use and meat consumption.")
    elif total > 5000:
        print("🙂 Around the average, but there’s room for improvement.")
    else:
        print("✅ Great! Your footprint is lower than average.")

    # --- Bar chart ---
    plt.figure(figsize=(8, 5))
    plt.bar(categories.keys(), categories.values())
    plt.title("CO₂ Footprint by Category")
    plt.ylabel("kg of CO₂ per year")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    calculate_co2()
