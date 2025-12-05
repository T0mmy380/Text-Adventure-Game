from Src.Types.TypeChart import TypeChart

def main():

    chart = TypeChart()

    grass_weak = [
        chart.get_effectiveness("Grass", "Grass"),
        chart.get_effectiveness("Grass", "Water"),
        chart.get_effectiveness("Grass", "Fire")
    ]

    water_weak = [
        chart.get_effectiveness("Water", "Grass"),
        chart.get_effectiveness("Water", "Water"),
        chart.get_effectiveness("Water", "Fire")
    ]

    fire_weak = [
        chart.get_effectiveness("Fire", "Grass"),
        chart.get_effectiveness("Fire", "Water"),
        chart.get_effectiveness("Fire", "Fire")
    ]

    print(grass_weak)
    print("\n")
    print(water_weak)
    print("\n")
    print(fire_weak)




if __name__ == "__main__":
    main()
