//funtion for the carbon footprint calculation
function carbon_print_calc() {
    const carbon_data = document.getElementById("id_co2_data").value;
    const co2_emmissions = document.getElementById("id_co2_emmissions").value;
    let result = co2_emmissions * carbon_data;
    window.alert("Your Carbon Footprint is: " + result)
}

//funtion for the energy usage calculation
function energy_print_calc() {
    const powerUsage = document.getElementById("id_power_usage").value;
    const timeOn = document.getElementById("id_time_on").value;
    let result = powerUsage * timeOn;

    window.alert("Your Power Usage per day is: " + result + "w")
}