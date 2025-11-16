# === node start up ===

# system functions
radio.on()
radio.set_group(1)
radio.set_transmit_power(7)

datalogger.set_column_titles("reciving node", "sending node", "msg data")

# node configurations
node_config = {
    "Node_ID": "SN-1",
    "firmware": "0.1",
    "active": True
}

network_config = {
    "network_ID": node_config["Node_ID"],
    "SN_network": ["SN-1", "SN-2"],
    "UN_network": ["UN-1", "UN-2"]
}
