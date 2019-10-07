from IPython.display import Javascript, display
import json

def _add_tags(tags):
    assert(all(map(lambda t: isinstance(t, str), tags)))
    display(Javascript(
        """
        require(['addTags'], function(addTags) {
            addTags(element, {0:s});
        });
        """.format(json.dumps(tags))
    ))
