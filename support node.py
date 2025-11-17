# === node start up ===
import JSON


# system functions
radio.on()
radio.set_group(1)
radio.set_transmit_power(7)



# node configurations
node_config = {
    "Node_ID": "SN-1",
    "firmware": "0.1",
    "radio_state": True,
    "recived_messages": ["7"]
}

network_config = {
    "network_ID": node_config["Node_ID"],
    "SN_network": ["SN-1", "SN-2"],
    "UN_network": ["UN-1", "UN-2"]
}

msg_data = {
    "Type": "user message",
    "Message_Cotains": 0,
    "Sending_node": "UN-1",
    "UN_recived": [""],
    "SN_recived": [""],
    "UMID": 8465937960
}

# ran without errors
basic.show_leds("""
. . # . .
. # # # .
# # # # #
. # # # .
. . # . .
""")


# === functions ===

# === network handaling ===

#   message recived handaling

def msg_recevied(string):
    
    msg_data = JSON.parse(string)
    bounce_msg = False
    

    if msg_data["msg type"] == "user message":
        
        # checks if all user nodes have gotten the message form sender
        #might need to use the message ID to stop the message form bouncic to much
        try:

            for node in network_config["UN_network"]:
            
                if node not in msg_data["UN_recived"]:
                    bounce_msg = True
                    break
        finally:
            pass
        
        if node_config["Node_ID"] in msg_data["SN_recived"]:
            msg_data["SN_recived"] = msg_data["SN_recived"] + node_config["Node_ID"]
            bounce_msg = False
    
    if bounce_msg == True:
        msg_sterlaized = JSON.stringify(msg_data) 
        radio.send_string(msg_sterlaized)

def toggle_radio():
    if node_config["radio_state"] == True:
        radio.off()
        node_config["radio_state"] = False
        basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
        basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    else:
        radio.on()
        node_config["radio_state"] = True
        basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
        basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)




        




# === main code ===

def on_forever():
    radio.on_received_string(msg_recevied)
    if input.logo_is_pressed():
        toggle_radio()


basic.forever(on_forever)
