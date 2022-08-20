"""
Assemble all the words from static variables.
"""
import random

from story_generator.static_variables import TIME, PROPER, PLACE, VERB


class StoryGenerator:
    """
    Class to build a story.
    """
    _time = TIME
    _proper = PROPER
    _place = PLACE
    _verb = VERB

    def get_time(self) -> str:
        """
        Gets the period of time.

        Returns:
             str:
                The period of time.
        """
        return random.choice(self._time)

    def get_proper(self) -> str:
        """
        Gets the subject of the story.

        Returns:
             str:
                The subject of the story line.
        """
        return random.choice(self._proper)

    def get_place(self) -> str:
        """
        Gets the place for the story line.

        Returns:
             str:
                The place of the story line.
        """
        return random.choice(self._place)

    def get_verb(self):
        """
        Gets the verb in the story line.

        Returns:
             str:
                The verb of the story line.
        """
        return random.choice(self._verb)

    def get_last(self):
        """
        Gets the object of the story line.

        Returns:
             str:
                The object of the story line.
        """
        return random.choice(self._place)

    def get_complete_line(self):
        """
        Gets the complete story line.

        Returns:
             str:
                The complete story line.
        """
        return f"{self.get_time()}, {self.get_proper()} was " \
               f"{self.get_verb()} in {self.get_last()}"
