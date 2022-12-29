# A Database for a platform providing online circuit manufacture orders.

1. A database schema that stores the following informations:

`user`: This is a table that contains the information of any customer and plant owner

* `USER_ID:` The customer and plant owner's identifier that determines other attributes. An integer. AUTO_INCREMENT.
* `FIRST_NAME:` The first name of a customer or a plant owner. At most 20 characters.
* `LAST_NAME:` The last name of a customer or a plant owner. At most 20 characters.
* `PHONE_NUMBER:` The phone number of a customer or a plant owner.  At most 20 characters, and character '.' is allowed for a phone number.
* `COUNTRY_NAME:` Should not be empty. The name of some country.
* `PROVINCE:`Should not be empty. The name of some province.
* `ROLE:` The idertifier for distinguish customer and plant owner. At most 30 characters.
* `STREET_ADDRESS:` A string that is no more than 40 characters for street address. Might be empty
* `PASSWORD:` A string that is no more than 40 characters for password.

`package:` This is a table that contains the information of the ordered package by customers.

* `USER_ID:` An attribute having the same format as `user.USER_ID` that can not be empty.
* `PACKAGE_ID:` The package identifier that determines other attributes. An integer. AUTO_INCREMENT.
* `BUDGET:` An attribute describes the budget for a package.  A float number with at most 10 digits to the left of the decimal point, and 2 to the right of it.
* `CREATE_TIME:`The date when the package was created.
* `DEADLINE:`The date when the package was supposed to be finished.

`state`: This is a table that describes the processing state of packages.

* `PACKAGE_ID: ` An attribute having the same format as `package.PACKAGE_ID` that can not be empty.
* `START_TIME: ` The date when the package was started to be processed.
* `END_TIME: ` The date when the processing of the package was finished.
* `STATE_NAME:` An attribute describe the processing state of packages, i.e. processing; cancelled; finished; waiting

`plant`: This is a table that contains the information of any plant.

* `PLANT_ID: ` The plant identifier that determines other attributes. An integer. AUTO_INCREMENT.
* `PLANT_NAME: ` The name of the plant. At most 20 characters.
* `PHONE_NUMBER`:  The phone number of the plant having the same format as `user.PHONE_NUMBER`.
* `BOSS_ID`:  An attribute having the same format as `user.USER_ID` that can not be empty.
* `COUNTRY_NAME`:  The location identifier of the plant having the same format as `user.COUNTRY_NAME`.
* `PROVINCE:  `The location identifier of the plant having the same format as `user.PROVINCE`.
* `STREET_ADDRESS: ` The location identifier of the plant having the same format as `user.STREET_ADDRESS`.

`machine_type`: This is a table that describes the types of machines.

* `MACHINE_NAME: ` The name of the machine. Can not be empty. At most 20 characters. Together with `MACHINE_VERSION` determines other attibutes.
* `MACHINE_VERSION:` The version identifier of the machine. Can not be empty. A integer. Together with `MACHINE_NAME` determines other attributes.
* `PRICE:` The price of the machine. A float.

`machine`: This is a table that describes machines in different plants.

* `MACHINE_NAME:  `The name of the machine. Can not be empty. At most 20 characters. Together with `MACHINE_VERSION` determines other attibutes.
* `MACHINE_VERSION: `The version identifier of the machine. Can not be empty. A integer. Together with `MACHINE_NAME` determines other attributes.
* `PRICE:` The price of the machine. A float.
* `PLANT_ID: ` An attribute having the same format as `plant.PLANT_ID`.
* `MACHINE_ID: ` The machine identifier that determines other attributes. An integer. AUTO_INCREMENT.
* `PLANT_LABEL: ` A attribute describe which plants does the machine belongs to. At most 10 characters.
*  `STATE: ` A attribute describe the state of the machine, i.e. working; free... 

`chip_type`: This is a table that describes the types of chips.

* `CHIP_NAME: `The name of the chip. Can not be empty. At most 20 characters. Together with `CHIP_VERSION` determines other attributes.
* `CHIP_VERSION: `The version identifier of the chip. Can not be empty. At most 20 characters. Together with `CHIP_NAME` determines other attributes.
* `PRICE: ` The price of the chip. A float.

`chip`: This is a table that describes different chips.

* `CHIP_NAME: ` An attribute having the same format as `chip_type.CHIP_NAME`.
* `CHIP_VERSION`: An attribute having the same format as `chip_type.CHIP_VERSION.`
* `PRICE: ` The price of the chip. A float.
* `PACKAGE_ID: `An attribute describe which package does the chip belongs to, having the same format as `package.PACKAGE_ID`.
* `CHIP_ID:` The chip identifier that determines other attributes. An integer. AUTO_INCREMENT
* `PLANT_ID :` A attribute describe which plant is manufacturing this chip.

`operation_type`: This is a table that describe different types of operations that manufacture chips.

* `OPERATION_NAME:` The operation identifier that describe the name of the operation.

`operation`: This is a table that describes different operations' processing information.

* `OPERATION_ID:` The operation identifier that determines other attributes. An integer.
* `OPERATION_NAME: `An attribute having the same format as `operation_type.OPERATION_NAME.`
* `START_TIME: `An attribute that describe when the operation starts. A datetime data type.
* `END_TIME:` An attribute that describe when the operation ends. A datetime  data type.

`operation_with_machine:` This is a relationship table that describes the relationship between operation and machine.

* `OPERATION_ID: ` An attribute having the same format as `operation.OPERATION_ID.`
* `MACHINE_ID: `An attribute having the same format as `machine.MACHINE_ID.`
* `START_TIME: `An attribute that describes when the machine starts to process the operation. A datetime data type.
* `END_TIME: `An attribute that describes when the machine finishes the operation. A datetime data type.
* `PRIMARY KEY: ` OPERATION_ID + CHIP_ID
* `FOREIGN KEY`:  OPERATION_ID references operation; CHIP_ID references chip.

`operation_with_chip:` This is a relatinship table that describes the relationship between operation and chip.

* `OPERATION_ID: ` An attribute having the same format as `operation.OPERATION_ID.`
* `CHIP_ID: `An attribute having the same format as `chip.CHIP_ID.`
* `PRIMARY KEY: ` OPERATION_ID + MACHINE_ID
* `FOREIGN KEY`:  OPERATION_ID references operation; MACHINE_ID references machine.

`plant_with_package:` This is a relationship table that describe the relationship between plant and package.

* `PACKAGE_ID: `An attribute having the same format as `package.PACKAGE_ID.`
* `PLANT_ID: `An attribute having the same format as `plant.PLANT_ID.`
* `PRIMARY KEY: `PACKAGE_ID+PLANT_ID
* `FOREIGN KEY:` PACKAGE_ID references package; PLANT_ID references plant.

`chip_type_with_operation_type:` This is a relationship table that describe the relationship between chip_type and operation_type. Different types of chips need different types of operations.

* `ODER_OP: ` An attribute that describe the order of the operation in a chip manufacturing.
* `OPERATION_NAME: ` An attribute having the same format as `operation_type.OPERATION_NAME.`
* `CHIP_NAME: `An attribute having the same format as `chip_type.CHIP_NAME.`
* `CHIP_VERSION: `An attribute having the same format as `chip_type.CHIP_VERSION.`
* `PRIMARY KEY: `OPERATION_NAME+CHIP_NAME+CHIP_VERSION.
* `FOREIGN KEY: `OPERATION_NAME references operation type; CHIP_NAME and CHIP_VERSION references chip_type.

`machine_type_with_operation_type:`This is a relationship table that describe the relationship between machine_type and operation_type. Different types of machines can handle different types of operations.

* `OPERATION_NAME:`An attribute having the same format as `operation_type.OPERATION_NAME.`
* `MACHINE_NAME: `An attribute having the same format as `machine_type.MACHINE_NAME.`
* `MACHINE_VERSION:` An attribute having the same format as `machine_type.MACHINE_VERSION.`
* `EXPENSE: `An attribute that describes how much dose certain type of machine needs to process certain type of operation. An integer.
* `DURATION: `An attribute that describes how long does certain type of machine needs to process certain type of operation. An integer.
* `PRIMARY KEY:` OPERATION_NAME+MACHINE_NAME+MACHINE_VERSION.
* `FOREIGN KEY: `OPERATION_NAME references operation_type; MACHINE_NAME and MACHINE_VERSION reference machine_type.


