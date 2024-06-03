import pytest
import json
import decoder
import sys


@pytest.fixture
def format_strings():
    return {
        "20185088": "%s %s initialized!",
        "20185092": "<inf>",
        "20185096": "QSPI",
        "20185100": "%s %s:  FLASH_Init",
        "20185104": "flash",
        "20185108": "%s %s:  Header loaded. Partitions table offset: 0x%04X",
        "20185112": "%s %s:  Partition table loaded",
        "20185116": "%s %s:  History length %d, last flag at %04X.",
        "20185120": "bf",
        "20185124": "%s %s:  Checking flag[%d] 0x%x",
        "20185128": "%s %s:  Continue boot: SecOs was loaded some time ago!",
        "20185132": "<wrn>",
        "20185136": "%s %s:  Append 0x%X flag at %04X",
        "20185140": "%s data ADDR: %08X, SIZE: %d",
        "20185144": "Write",
        "20185148": "%s %s:  Partition %d offset: 0x%04X",
        "20185152": "%s %s:  Section data %d bytes loaded at 0x%X",
        "20185156": "%s %s:  Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: 1024]",
        "20185160": "%s %s:  MemToLock: 0x%08x. Size: %d",
        "20185164": "memory",
        "20185168": "%s %s:  %s: Loading section data to 0137c400",
        "20185172": "utils",
        "20185176": "BL0K",
        "20185180": "%s %s:  Speed up: RN is provided!",
        "20185184": "crypto",
        "20185188": "%s %s:  %s: Section signature is valid",
        "20185192": "%s Key was added to context",
        "20185196": "BL0",
        "20185200": "%s %s:  Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: %u]",
        "20185204": "%s %s:  MemToLock: 0x%08X. Size: %d",
        "20185208": "%s %s:  %s: Loading section data to 01300000",
        "20185212": "BL1D",
        "20185216": "%s %s:  Slot %d [0x%08X-0x%08X] is free now",
        "20185220": "!!! %s: DONE ON PARTITION %d !!!",
        "20185224": "%s %s:  Jump to: 0x%X",
        "20185228": "[%08u] %s %s: Device id %02x %02x %02x is Ok",
        "20185232": "spi_flash",
        "20185236": "[%08u] %s %s: LPDDR Tool starting task",
        "20185240": "lpddr_tool",
        "20185244": "[%08u] %s %s: Starting BL1 version: %s",
        "20185248": "bl1",
        "20185252": "1.0.0-stable",
        "20185256": "[%08u] %s %s: MxManager_Init: Initializing MX-manager..",
        "20185260": "<dbg>",
        "20185264": "mx_manager",
        "20185268": "[%08u] %s %s: MX hardware initialization is skipped (already initialized)",
        "20185272": "[%08u] %s %s: Init: mx-region#%d: page=%xh; refs=%d",
        "20185276": "[%08u] %s %s: MX-manager initialized",
        "20185280": "[%08u] %s %s: %s: Initializing SCMI..",
        "20185284": "platform_init",
        "20185288": "[%08u] %s %s: Platform initialization done!",
        "20185292": "[%08u] %s %s: %s: Initializing SPI-flash..",
        "20185296": "secure_boot_init",
        "20185300": "[%08u] %s %s: %s device is detected",
        "20185304": "d50s64qdi@0",
        "20185308": "[%08u] %s %s: FLASH_Init",
        "20185312": "[%08u] %s %s: Header loaded. Partitions table offset: 0x%X",
        "20185316": "[%08u] %s %s: Partition table loaded",
        "20185320": "[%08u] %s %s: [Fetching BL1 public key]",
        "20185324": "[%08u] %s %s: Partition %d offset: 0x%X",
        "20185328": "[%08u] %s %s: Section data %d bytes loaded at 0x%X",
        "20185332": "[%08u] %s %s: Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: 1024]",
        "20185336": "[%08u] %s %s: Mapping of address range requested [%02X%08Xh; %02X%08Xh)..",
        "20185340": "[%08u] %s %s: MapRange: first_page=%xh, last_page=%xh",
        "20185344": "[%08u] %s %s: ObtainHandle: obtained handle=%d",
        "20185348": "[%08u] %s %s: MapRange: selected %d mx-region(s) starting from %d",
        "20185352": "[%08u] %s %s: ConfigSetOfMxRegions: mx-region#%d: addr=%x_%08xh, refs=%d",
        "20185356": "[%08u] %s %s: MapRange: mapped to reduced address %08Xh, used regions [%d;%d)",
        "20185360": "[%08u] %s %s: (%s) Loading section data starting at %X_%08Xh",
        "20185364": "BL1K",
        "20185368": "[%08u] %s %s: GetReducedAddr: address conversion: %02X%08Xh --> %08Xh",
        "20185372": "[%08u] %s %s: (%s) Loaded",
        "20185376": "[%08u] %s %s: Speed up: RN is provided!",
        "20185380": "[%08u] %s %s: (%s) Section signature is valid",
        "20185384": "[%08u] %s %s: UnmapRange: unmapping of address range requested (handle=%d)..",
        "20185388": "[%08u] %s %s: UnmapRange: mx-region#%d: refs=%d",
        "20185392": "[%08u] %s %s: range starting at %02X%08Xh (sz: %d) is unmapped",
        "20185396": "[%08u] %s %s: FreeHandle: handle=%d is released",
        "20185400": "[%08u] %s %s: LPDDR initialization...",
        "20185404": "%s:  LPDDR4 is configured with %d pstate",
        "20185408": "%s:  Setup LPDDR DfiClk line: %d MHz",
        "20185412": "%s:  Setup LPDDR clock done",
        "20185416": "%s:  Uploading code section for 1D Training to DDR PHY",
        "20185420": "%s:  DDRPHY code file size: %d bytes",
        "20185424": "%s:  Done uploading code section to DDR PHY",
        "20185428": "%s:  %s()",
        "20185432": "dwc_ddrphy_phyinit_userCustom_E_setDfiClk",
        "20185436": "%s:  Uploading data section for 1D Training to DDR PHY",
        "20185440": "%s:  DDRPHY data file size: %d bytes",
        "20185444": "%s:  Done uploading data section to DDR PHY",
        "20185448": "%s:  [%s()] PhyMaster_PhyInterruptEnable = 0x%04X",
        "20185452": "en_phy_ints",
        "20185456": "dwc_ddrphy_phyinit_userCustom_G_waitFwDone",
        "20185460": "%s:  phy pub message: training has run successfully (firmware complete)",
        "20185464": "dwc_ddrphy_phyinit_userCustom_H_readMsgBlock",
        "20185468": "%s:  Load PIE Production code: DramDataWidth=%d EnableHighClkSkewFix=%s",
        "20185472": "NO",
        "20185476": "dwc_ddrphy_phyinit_userCustom_customPostTrain",
        "20185480": "dwc_ddrphy_phyinit_userCustom_J_enterMissionMode",
        "20185484": "%s:  LPDDR4 Initialization done",
        "20185488": "%s:  ==================================================",
        "20185492": "%s:  %s @ [%08X] = 0x%08X",
        "20185496": "MSTR",
        "20185500": "%s:  %s[%u] @ [%08X] = 0x%08X",
        "20185504": "INIT",
        "20185508": "DRAMTMG",
        "20185512": "DFIPHYMSTR",
        "20185516": "DFIMISC",
        "20185520": "DFILPCFG0",
        "20185524": "DFITMG0",
        "20185528": "DFITMG1",
        "20185532": "DFITMG2",
        "20185536": "DFIUPD0",
        "20185540": "DFIUPD1",
        "20185544": "DFIUPD2",
        "20185548": "ADDRMAP",
        "20185552": "RANKCTL",
        "20185556": "RANKCTL1",
        "20185560": "RFSHCTL0",
        "20185564": "RFSHCTL1",
        "20185568": "RFSHCTL3",
        "20185572": "RFSHTMG",
        "20185576": "RFSHTMG1",
        "20185580": "ODTMAP",
        "20185584": "ZQCTL0",
        "20185588": "ZQCTL1",
        "20185592": "ZQCTL2",
        "20185596": "DERATECTL",
        "20185600": "UMCTL2_REGS_DCH1.DERATECTL",
        "20185604": "DERATEEN",
        "20185608": "DERATEINT",
        "20185612": "PWRCTL",
        "20185616": "UMCTL2_REGS_DCH1.PWRCTL",
        "20185620": "PWRTMG",
        "20185624": "HWLPCTL",
        "20185628": "SCHED",
        "20185632": "CRCPARCTL0",
        "20185636": "DBG",
        "20185640": "[%08u] %s %s: Setting up LPDDR access",
        "20185644": "[%08u] %s %s: LPDDR Memtest preparation",
        "20185648": "[%08u] %s %s: LPDDR Memtest start",
        "20185652": "[%08u] %s %s: LPDDR Memtest done",
        "20185656": "[%08u] %s %s: range starting at %02X%08Xh (sz: %u) is unmapped",
        "20185660": "Starting DRAM Stress test with DMA",
        "20185664": "Iteration size is %u bytes",
        "20185668": "Start SRAM => DDR at offset %08X",
        "20185672": "      SRC: %08X %08X %08X %08X %08X %08X %08X %08X",
        "20185676": "           ...",
        "20185680": "           %08X %08X %08X %08X %08X %08X %08X %08X",
        "20185684": "      DDR => SRAM at offset %08X",
        "20185688": "      Compare buffers",
        "20185692": "      Iteration done, SRAM => DDR: %u ticks, DDR => SRAM: %u ticks"
    }


@pytest.fixture
def binary_path(tmp_path):
    binary_file = tmp_path / "test_binary.bin"
    binary_file.write_bytes(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a')
    return str(binary_file)


@pytest.fixture
def json_path(tmp_path, format_strings):
    json_file = tmp_path / "test_json.json"
    with open(json_file, 'w') as f:
        json.dump(format_strings, f)
    return str(json_file)


# Проверяет, что форматированные строки правильно читаются из JSON
def test_read_json_format_strings(json_path):
    expected_format_strings = {
        "20185088": "%s %s initialized!",
        "20185092": "<inf>",
        "20185096": "QSPI",
        "20185100": "%s %s:  FLASH_Init",
        "20185104": "flash",
        "20185108": "%s %s:  Header loaded. Partitions table offset: 0x%04X",
        "20185112": "%s %s:  Partition table loaded",
        "20185116": "%s %s:  History length %d, last flag at %04X.",
        "20185120": "bf",
        "20185124": "%s %s:  Checking flag[%d] 0x%x",
        "20185128": "%s %s:  Continue boot: SecOs was loaded some time ago!",
        "20185132": "<wrn>",
        "20185136": "%s %s:  Append 0x%X flag at %04X",
        "20185140": "%s data ADDR: %08X, SIZE: %d",
        "20185144": "Write",
        "20185148": "%s %s:  Partition %d offset: 0x%04X",
        "20185152": "%s %s:  Section data %d bytes loaded at 0x%X",
        "20185156": "%s %s:  Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: 1024]",
        "20185160": "%s %s:  MemToLock: 0x%08x. Size: %d",
        "20185164": "memory",
        "20185168": "%s %s:  %s: Loading section data to 0137c400",
        "20185172": "utils",
        "20185176": "BL0K",
        "20185180": "%s %s:  Speed up: RN is provided!",
        "20185184": "crypto",
        "20185188": "%s %s:  %s: Section signature is valid",
        "20185192": "%s Key was added to context",
        "20185196": "BL0",
        "20185200": "%s %s:  Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: %u]",
        "20185204": "%s %s:  MemToLock: 0x%08X. Size: %d",
        "20185208": "%s %s:  %s: Loading section data to 01300000",
        "20185212": "BL1D",
        "20185216": "%s %s:  Slot %d [0x%08X-0x%08X] is free now",
        "20185220": "!!! %s: DONE ON PARTITION %d !!!",
        "20185224": "%s %s:  Jump to: 0x%X",
        "20185228": "[%08u] %s %s: Device id %02x %02x %02x is Ok",
        "20185232": "spi_flash",
        "20185236": "[%08u] %s %s: LPDDR Tool starting task",
        "20185240": "lpddr_tool",
        "20185244": "[%08u] %s %s: Starting BL1 version: %s",
        "20185248": "bl1",
        "20185252": "1.0.0-stable",
        "20185256": "[%08u] %s %s: MxManager_Init: Initializing MX-manager..",
        "20185260": "<dbg>",
        "20185264": "mx_manager",
        "20185268": "[%08u] %s %s: MX hardware initialization is skipped (already initialized)",
        "20185272": "[%08u] %s %s: Init: mx-region#%d: page=%xh; refs=%d",
        "20185276": "[%08u] %s %s: MX-manager initialized",
        "20185280": "[%08u] %s %s: %s: Initializing SCMI..",
        "20185284": "platform_init",
        "20185288": "[%08u] %s %s: Platform initialization done!",
        "20185292": "[%08u] %s %s: %s: Initializing SPI-flash..",
        "20185296": "secure_boot_init",
        "20185300": "[%08u] %s %s: %s device is detected",
        "20185304": "d50s64qdi@0",
        "20185308": "[%08u] %s %s: FLASH_Init",
        "20185312": "[%08u] %s %s: Header loaded. Partitions table offset: 0x%X",
        "20185316": "[%08u] %s %s: Partition table loaded",
        "20185320": "[%08u] %s %s: [Fetching BL1 public key]",
        "20185324": "[%08u] %s %s: Partition %d offset: 0x%X",
        "20185328": "[%08u] %s %s: Section data %d bytes loaded at 0x%X",
        "20185332": "[%08u] %s %s: Manifest loaded. [load_addr: %08X_%08Xh; start_addr: %08X_%08Xh; data_sz: 1024]",
        "20185336": "[%08u] %s %s: Mapping of address range requested [%02X%08Xh; %02X%08Xh)..",
        "20185340": "[%08u] %s %s: MapRange: first_page=%xh, last_page=%xh",
        "20185344": "[%08u] %s %s: ObtainHandle: obtained handle=%d",
        "20185348": "[%08u] %s %s: MapRange: selected %d mx-region(s) starting from %d",
        "20185352": "[%08u] %s %s: ConfigSetOfMxRegions: mx-region#%d: addr=%x_%08xh, refs=%d",
        "20185356": "[%08u] %s %s: MapRange: mapped to reduced address %08Xh, used regions [%d;%d)",
        "20185360": "[%08u] %s %s: (%s) Loading section data starting at %X_%08Xh",
        "20185364": "BL1K",
        "20185368": "[%08u] %s %s: GetReducedAddr: address conversion: %02X%08Xh --> %08Xh",
        "20185372": "[%08u] %s %s: (%s) Loaded",
        "20185376": "[%08u] %s %s: Speed up: RN is provided!",
        "20185380": "[%08u] %s %s: (%s) Section signature is valid",
        "20185384": "[%08u] %s %s: UnmapRange: unmapping of address range requested (handle=%d)..",
        "20185388": "[%08u] %s %s: UnmapRange: mx-region#%d: refs=%d",
        "20185392": "[%08u] %s %s: range starting at %02X%08Xh (sz: %d) is unmapped",
        "20185396": "[%08u] %s %s: FreeHandle: handle=%d is released",
        "20185400": "[%08u] %s %s: LPDDR initialization...",
        "20185404": "%s:  LPDDR4 is configured with %d pstate",
        "20185408": "%s:  Setup LPDDR DfiClk line: %d MHz",
        "20185412": "%s:  Setup LPDDR clock done",
        "20185416": "%s:  Uploading code section for 1D Training to DDR PHY",
        "20185420": "%s:  DDRPHY code file size: %d bytes",
        "20185424": "%s:  Done uploading code section to DDR PHY",
        "20185428": "%s:  %s()",
        "20185432": "dwc_ddrphy_phyinit_userCustom_E_setDfiClk",
        "20185436": "%s:  Uploading data section for 1D Training to DDR PHY",
        "20185440": "%s:  DDRPHY data file size: %d bytes",
        "20185444": "%s:  Done uploading data section to DDR PHY",
        "20185448": "%s:  [%s()] PhyMaster_PhyInterruptEnable = 0x%04X",
        "20185452": "en_phy_ints",
        "20185456": "dwc_ddrphy_phyinit_userCustom_G_waitFwDone",
        "20185460": "%s:  phy pub message: training has run successfully (firmware complete)",
        "20185464": "dwc_ddrphy_phyinit_userCustom_H_readMsgBlock",
        "20185468": "%s:  Load PIE Production code: DramDataWidth=%d EnableHighClkSkewFix=%s",
        "20185472": "NO",
        "20185476": "dwc_ddrphy_phyinit_userCustom_customPostTrain",
        "20185480": "dwc_ddrphy_phyinit_userCustom_J_enterMissionMode",
        "20185484": "%s:  LPDDR4 Initialization done",
        "20185488": "%s:  ==================================================",
        "20185492": "%s:  %s @ [%08X] = 0x%08X",
        "20185496": "MSTR",
        "20185500": "%s:  %s[%u] @ [%08X] = 0x%08X",
        "20185504": "INIT",
        "20185508": "DRAMTMG",
        "20185512": "DFIPHYMSTR",
        "20185516": "DFIMISC",
        "20185520": "DFILPCFG0",
        "20185524": "DFITMG0",
        "20185528": "DFITMG1",
        "20185532": "DFITMG2",
        "20185536": "DFIUPD0",
        "20185540": "DFIUPD1",
        "20185544": "DFIUPD2",
        "20185548": "ADDRMAP",
        "20185552": "RANKCTL",
        "20185556": "RANKCTL1",
        "20185560": "RFSHCTL0",
        "20185564": "RFSHCTL1",
        "20185568": "RFSHCTL3",
        "20185572": "RFSHTMG",
        "20185576": "RFSHTMG1",
        "20185580": "ODTMAP",
        "20185584": "ZQCTL0",
        "20185588": "ZQCTL1",
        "20185592": "ZQCTL2",
        "20185596": "DERATECTL",
        "20185600": "UMCTL2_REGS_DCH1.DERATECTL",
        "20185604": "DERATEEN",
        "20185608": "DERATEINT",
        "20185612": "PWRCTL",
        "20185616": "UMCTL2_REGS_DCH1.PWRCTL",
        "20185620": "PWRTMG",
        "20185624": "HWLPCTL",
        "20185628": "SCHED",
        "20185632": "CRCPARCTL0",
        "20185636": "DBG",
        "20185640": "[%08u] %s %s: Setting up LPDDR access",
        "20185644": "[%08u] %s %s: LPDDR Memtest preparation",
        "20185648": "[%08u] %s %s: LPDDR Memtest start",
        "20185652": "[%08u] %s %s: LPDDR Memtest done",
        "20185656": "[%08u] %s %s: range starting at %02X%08Xh (sz: %u) is unmapped",
        "20185660": "Starting DRAM Stress test with DMA",
        "20185664": "Iteration size is %u bytes",
        "20185668": "Start SRAM => DDR at offset %08X",
        "20185672": "      SRC: %08X %08X %08X %08X %08X %08X %08X %08X",
        "20185676": "           ...",
        "20185680": "           %08X %08X %08X %08X %08X %08X %08X %08X",
        "20185684": "      DDR => SRAM at offset %08X",
        "20185688": "      Compare buffers",
        "20185692": "      Iteration done, SRAM => DDR: %u ticks, DDR => SRAM: %u ticks"
    }
    result = decoder.read_json_format_strings(json_path)
    assert result == expected_format_strings


# Проверяет правильность вычисления CRC8
def test_crc8_check():
    data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a'
    expected_crc8 = 164
    assert decoder.crc8_check(data) == expected_crc8


# Проверяет правильность разбора аргументов
def test_parse_arguments(format_strings):
    format_string = '%s %d %x'
    data = b'\x05\x00\x00\x00'
    expected_arguments = ['<unknown string at 5>']
    assert decoder.parse_arguments(format_string, data, format_strings) == expected_arguments


def test_parse_binary_log_file(binary_path, json_path, capsys):
    format_strings = decoder.read_json_format_strings(json_path)
    decoder.parse_binary_log_file(binary_path, format_strings)
    captured = capsys.readouterr()

    # Проверка ожидаемых выводов
    assert "Processing page 0\n" in captured.err
    assert "SyncFrame - CRC8: 1, Expected CRC8: 14, Size: 2, StringAddr: 100992003, Timestamp: 168364039" in captured.err


def test_main(capsys, binary_path, json_path):
    # Сохраняем оригинальные аргументы
    original_argv = sys.argv
    # Устанавливаем новые аргументы для теста
    sys.argv = ["decoder.py", binary_path, "-m", json_path]

    try:
        decoder.main()
    finally:
        sys.argv = original_argv

    captured = capsys.readouterr()

    # Возвращаем оригинальные аргументы
    sys.argv = original_argv

    assert "Binary file" in captured.err
    assert "JSON file" in captured.err