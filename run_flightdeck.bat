@echo off
cd /d "C:\Users\Harold Pelzer\OneDrive\Desktop\Forex_Bootcamp"

echo Starting FlightDeck full run...

python flightdeck_pipeline.py
python update_scores.py
python update_trends.py
python update_research_scores.py
python update_daily_structure.py
python update_final_scores.py
python update_dxy_proxy.py
python send_flightdeck_alerts.py

echo FlightDeck full run complete.