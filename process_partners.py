import json
import csv


def process_json_to_csv(json_file, csv_file):
    with open(json_file, "r") as file:
        data = json.load(file)

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(
            [
                "name",
                "description",
                "specializations",
                "expertises",
                "premierPartner",
                "initiatives",
                "products",
                "regions",
            ]
        )

        for item in data:
            name = item.get("displayName", "")
            description = item.get("description", "")

            # Extract specialization names
            specializations_data = item.get("programData", {}).get(
                "partnerSpecializations", []
            )
            specializations = ", ".join(
                [spec.get("specializationName", "") for spec in specializations_data]
            )

            expertises = ", ".join(item.get("programData", {}).get("expertises", []))
            premierPartner = item.get("programData", {}).get("level", "") == "level_2"
            initiatives = ", ".join(item.get("programData", {}).get("initiatives", []))
            products = ", ".join(item.get("programData", {}).get("products", []))
            regions = ", ".join(item.get("programData", {}).get("regions", []))

            writer.writerow(
                [
                    name,
                    description,
                    specializations,
                    expertises,
                    premierPartner,
                    initiatives,
                    products,
                    regions,
                ]
            )


# Example usage
json_file_path = "partners.json"  # Replace with your JSON file path
csv_file_path = "output.csv"
process_json_to_csv(json_file_path, csv_file_path)
