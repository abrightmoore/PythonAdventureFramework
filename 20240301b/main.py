#   @TheWorldFoundry

class Graph:
    class Node:
        def __init__(self, label, data):
            self.label = label
            self.child = {}
            self.data = data
        
        def add_child(self, child_node):
            self.child[child_node.label] = child_node

    def __init__(self):
        self.nodes = {}
        self.vertices = {}
    
    def add_node(self, node):
        self.nodes[node.label] = node
    
    def add_vertex(self, source_node, target_node, vertex_label, vertex_value):
        self.add_node(source_node)
        self.add_node(target_node)
        source_node.add_child(target_node)
        self.vertices[(source_node.label, vertex_label, target_node.label)] = vertex_value

class UI:
    class UI_Output:
        def __init__(self):
            pass
            
        def display_text_lines(self, lines):
            for line in lines:
                print(line)


    class UI_Input:
        def __init__(self):
            pass
            
        def text_input_wait(self, prompt):
            user_input = input(prompt)
            return user_input
    
    def __init__(self):
        self.ui_out = self.UI_Output()
        self.ui_in = self.UI_Input()

class Game:
    KEY_DESC = "description"
    KEY_PROMPT = "prompt"
    STR_SEPERATOR = "_______________________"

    class Player:
        def __init__(self, location):
            self.location = location
            
    def __init__(self, universe, start_node):
        self.model = universe
        self.view = UI()
        self.players = [ self.Player(start_node) ]
        
    def run(self):
        for player in self.players:
            #   Process the area the player is within (current node)
            
            self.view.ui_out.display_text_lines(player.location.data[self.KEY_DESC])
            self.view.ui_in.text_input_wait(player.location.data[self.KEY_PROMPT])
            
room1 = Graph.Node( "Home Office", {})        
game = Game(Graph(), room1)
room1.data =    {   game.KEY_DESC : [
                        "You sit in a tall fabric chair, using a computer.",
                        "Your arms are carrying the weight of your frame on elbows resting on a hard wood desk.",
                        "Your finger tips lie gently on the keyboard.",
                    game.STR_SEPERATOR ],
                    game.KEY_PROMPT : "What will you type?   "
                }
game.run()