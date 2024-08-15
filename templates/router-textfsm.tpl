Value INTERFACE (\S+)
Value IP_ADDRESS (\S+)
Value STATUS (up|down|administratively down|unset)
Value PROTOCOL (up|down)

Start
 ^${INTERFACE}\s+${IP_ADDRESS}\s+\S+\s+\S+\s+${STATUS}\s+${PROTOCOL}\s* -> Record
 ^\s*$$ -> End