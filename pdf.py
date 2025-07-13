from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Environmental Studies Notes", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0)
        self.multi_cell(0, 10, title)
        self.ln(1)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.chapter_title("Module 3: Biodiversity and its Conservation")

content_module3 = """
- Introduction:
  Biodiversity refers to the variety of life forms on Earth. It exists at three levels:
  1. Genetic Diversity: Variety of genes within a species (e.g., different varieties of rice).
  2. Species Diversity: Variety of species within a region.
  3. Ecosystem Diversity: Variety of ecosystems (forests, deserts, wetlands, etc.).

- Biodiversity at Different Levels:
  - Global: Estimated 8.7 million species on Earth.
  - National: India has about 8% of the world’s biodiversity.
  - Local: Includes local flora and fauna, often unique to a region.

- India as a Mega-Diversity Nation:
  - One of the 17 mega-diverse countries.
  - Rich in endemic species.
  - Diverse climatic and topographic conditions.

- Hotspots of Biodiversity:
  - Regions with high endemic species and under severe threat.
  - India has four major hotspots: Himalayas, Indo-Burma, Western Ghats-Sri Lanka, and Sundaland (Nicobar Islands).

- Threats to Biodiversity:
  1. Habitat Loss: Due to deforestation, urbanization.
  2. Poaching: Illegal hunting and trade of wildlife.
  3. Man-Wildlife Conflicts: Encroachment and competition for resources.

- Endangered and Endemic Species in India:
  - Endangered: Bengal tiger, Asiatic lion, Indian rhino.
  - Endemic: Nilgiri Tahr, Lion-tailed macaque.
"""

pdf.chapter_body(content_module3)

pdf.chapter_title("Module 4: Social Issues and the Environment")

content_module4 = """
- From Unsustainable to Sustainable Development:
  - Unsustainable: Overuse of resources without regeneration.
  - Sustainable: Development that meets present needs without compromising future needs.

- Resettlement and Rehabilitation:
  - Due to development projects (dams, mines).
  - Issues: Loss of livelihood, cultural displacement, inadequate compensation.

- Environmental Ethics:
  - Concerned with moral relationships between humans and nature.
  - Issues: Resource exploitation, animal rights.
  - Solutions: Legal frameworks, education, eco-conscious behavior.

- Environmental Challenges:
  1. Climate Change: Caused by greenhouse gases.
  2. Global Warming: Rise in Earth’s temperature.
  3. Acid Rain: Caused by industrial emissions.
  4. Ozone Layer Depletion: Due to CFCs.
  5. Nuclear Accidents: Chernobyl, Fukushima.
  6. Holocaust: Environmental and social devastation due to human actions.

- Public Awareness:
  - Media, education, campaigns.
  - Role of individuals and NGOs in spreading awareness and initiating action.
"""

pdf.chapter_body(content_module4)

# Save the file
pdf.output("Biodiversity_and_Social_Issues_Notes.pdf")
