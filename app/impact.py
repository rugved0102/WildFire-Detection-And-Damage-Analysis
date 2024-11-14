import pandas as pd

# Load all datasets
def load_data(file_path_impact, file_path_weather_recovery):
    """Load vegetation, wildlife, weather, and recovery data from Excel files."""
    vegetation_data = pd.read_excel(file_path_impact, sheet_name='Vegetation Impact', engine='openpyxl')
    wildlife_data = pd.read_excel(file_path_impact, sheet_name='Wildlife Impact', engine='openpyxl')
    weather_data = pd.read_excel(file_path_weather_recovery, sheet_name='Weather Conditions', engine='openpyxl')
    recovery_data = pd.read_excel(file_path_weather_recovery, sheet_name='Recovery and Resilience Factors', engine='openpyxl')
    return vegetation_data, wildlife_data, weather_data, recovery_data

# Functions for Vegetation and Wildlife Impact
def get_vegetation_impact(region, vegetation_data):
    region_data = vegetation_data[vegetation_data['Region'].str.lower() == region.lower()]
    return region_data.iloc[0] if not region_data.empty else None

def get_wildlife_impact(region, wildlife_data):
    region_data = wildlife_data[wildlife_data['Region'].str.lower() == region.lower()]
    return region_data.iloc[0] if not region_data.empty else None

# Functions for Weather and Recovery Data
def get_weather_conditions(region, weather_data):
    region_data = weather_data[weather_data['Region'].str.lower() == region.lower()]
    return region_data.iloc[0] if not region_data.empty else None

def get_recovery_factors(region, recovery_data):
    region_data = recovery_data[recovery_data['Region'].str.lower() == region.lower()]
    return region_data.iloc[0] if not region_data.empty else None

# Main analysis function
def analyze_impact(region):
    """Analyze the impact of forest fire on vegetation, wildlife, weather, and recovery."""
    # Load all data
    vegetation_data, wildlife_data, weather_data, recovery_data = load_data(
        "vegetation_wildlife_impact.xlsx", "weather_and_recovery.xlsx"
    )
    
    # Get data for the specified region
    vegetation_impact = get_vegetation_impact(region, vegetation_data)
    wildlife_impact = get_wildlife_impact(region, wildlife_data)
    weather_conditions = get_weather_conditions(region, weather_data)
    recovery_factors = get_recovery_factors(region, recovery_data)
    
    return vegetation_impact, wildlife_impact, weather_conditions, recovery_factors
  
    print("Vegetation Impact:", vegetation_impact)
    print("Wildlife Impact:", wildlife_impact)
    print("Weather Conditions:", weather_conditions)
    print("Recovery Factors:", recovery_factors)
