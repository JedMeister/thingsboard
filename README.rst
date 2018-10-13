ThingsBoard - Open-source IoT Platform
======================================

ThingsBoard_ is an open-source IoT platform for data
collection, processing, visualization, and device management.
It enables device connectivity via industry standard IoT
protocols - MQTT, CoAP and HTTP and supports both cloud and
on-premises deployments. ThingsBoard combines scalability,
fault-tolerance and performance so you will never lose your data.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- ThnigsBoard installed from upstream deb.

  **Security note** : Updates to ThingsBoard may require supervision
  so they **ARE NOT** configured to install automatically. See 
  `ThingsBoard documentation`_ for updating ThingsBoard.

- ThingsBoard served via pre-configured Nginx
  reverse proxy.
- ThingsBoard using PostgreSQL DB backend
  (as recommneded).
- SSL support out of the box.
- Webmin modules for configuring PostgreSQL.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  PostgreSQL: username **postgres**
-  ThingsBoard Sysadmin: email set at firstboot
-  ThingsBoard 

.. _ThingsBoard: https://thingsboard.io/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _ThingsBoard documentation: https://thingsboard.io/docs/user-guide/install/upgrade-instructions/
