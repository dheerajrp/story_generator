"""
Main file
"""
from story_generator.assemble_words import StoryGenerator

story = StoryGenerator()
line = story.get_complete_line()
print(line)
