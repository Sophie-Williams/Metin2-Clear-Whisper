// 1.) Find this:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// 2.) Add after this:
#ifdef ENABLE_WHISPER_CLEAR
	PyModule_AddIntConstant(poModule, "ENABLE_WHISPER_CLEAR",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_WHISPER_CLEAR",	0);
#endif