# Class for classifying PDF elements
class ElementClassifier:
    def classify(self, elements):
        category_counts = {}
        for element in elements:
            category = str(type(element))
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
        return category_counts
