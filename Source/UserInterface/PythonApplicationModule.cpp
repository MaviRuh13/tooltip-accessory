// Arat - Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// Ekle - Add:
#ifdef ENABLE_TOOLTIP_ACCESSORY
	PyModule_AddIntConstant(poModule, "ENABLE_TOOLTIP_ACCESSORY", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_TOOLTIP_ACCESSORY", 0);
#endif