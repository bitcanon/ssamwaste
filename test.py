from ssam import ssam

ssam = ssam.WasteScheduler()

buildings = ssam.search_building('Flybogatan')

for building in buildings:
	print(building)

for waste_bin in ssam.get_waste_bins(buildings[0].id):
	print(waste_bin)
