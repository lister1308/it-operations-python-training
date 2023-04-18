from duckduckgo_search import ddg_images

query = "hond"  # de zoekopdracht

# zoek naar afbeeldingen met de zoekopdracht
results = ddg_images(query)

# controleer of er afbeeldingsresultaten zijn
if results:

    # haal de URL van de eerste afbeelding op
    image_url = results[0]['image']
    
    print(f"URL van de afbeelding: {image_url}")
else:
    print("Geen afbeeldingsresultaten gevonden.")
