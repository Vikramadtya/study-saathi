# The OSI Model

The International Organization for Standardization (ISO) researched different network models, and the result is the OSI-model which was released in 1984. Nowadays, most vendors build networks based on the OSI model.


This is the OSI model, which has seven layer

- Physical Layer: This layer describes stuff like voltage levels, timing, physical data rates, physical connectors, and so on.
- Data Link: This layer makes sure data is formatted the correct way, takes care of error detection, and makes sure data is delivered reliably. MAC Addresses and Ethernet frames are on the Data Link layer.
- Network: This layer takes care of connectivity and path selection (routing). This is where IPv4 and IPv6 live.
- Transport: The transport layer takes care of transport. 
  - TCP lives here; it’s a protocol that sends data in a reliable way.
  - UDP lives here; it’s a protocol that sends data in an unreliable way.
- Session: The session layer takes care of establishing, managing, and terminating sessions between two hosts.
- Presentation: This one will make sure that information is readable for the application layer by formatting and structuring the data. Most computers use the ASCII table for characters. If another computer would use another character like EBCDIC, then the presentation layer needs to “reformat” the data, so both computers agree on the same characters.
- Application: Here are your applications. E-mail, browsing the web (HTTP), FTP, and many more.

>  “People Do Need To See Pamela Anderson”

Going from the application layer all the way down to the physical layer is what we call encapsulation. Going from the physical layer and working your way up to the application layer is called de-encapsulation.

## Reference

- [Introduction to the OSI Model](https://networklessons.com/cisco/ccna-routing-switching-icnd1-100-105/introduction-to-the-osi-model)
