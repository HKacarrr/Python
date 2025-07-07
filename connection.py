import pymysql

# Database connection config (örnek, kendi ortamına göre düzenle)
DB_CONFIG = {
    'host': 'localhost',
    'port': 8889,
    'user': 'root',
    'password': 'root',
    'database': 'api',
}

# --- CREATE TABLE SCRIPTS ---

table_invoiceList = """
CREATE TABLE IF NOT EXISTS InvoiceList (
    invoiceAccountId INT NOT NULL,
    clientId INT NOT NULL,
    totalGrossAmount DECIMAL(9,2) NOT NULL,
    invoiceDate DATE NOT NULL,
    csvImportId INT,
    documentId INT,
    outstandingAmount DECIMAL(9,2) DEFAULT 0,
    totalNetAmount DECIMAL(9,2) DEFAULT 0,
    totalTaxAmount DECIMAL(9,2) DEFAULT 0,
    isDiscount BOOLEAN DEFAULT FALSE,
    invoiceType VARCHAR(15) DEFAULT 'RE',
    isCredit BOOLEAN DEFAULT FALSE,
    isCommit BOOLEAN DEFAULT FALSE,
    clientInvoiceNo INT DEFAULT 1,
    isDelete BOOLEAN DEFAULT FALSE,
    isReverseCharge BOOLEAN DEFAULT FALSE,
    invoicePartyName VARCHAR(300),
    invoicePartyAddress VARCHAR(145),
    invoicePartyStreet VARCHAR(145),
    invoicePartyDomain VARCHAR(150),
    invoicePartyZip VARCHAR(75),
    invoicePartyDebtor VARCHAR(50),
    invoicePartyEmail VARCHAR(150),
    invoicePartyVatId VARCHAR(40),
    invoicePartyCity VARCHAR(145),
    invoicePartyCountry VARCHAR(5),
    invoicePartyNumber VARCHAR(45),
    invoiceNo VARCHAR(45),
    currency VARCHAR(5) DEFAULT 'EUR',
    invoiceTypeData VARCHAR(50),
    invoicePartyAccountNo INT,
    exDocUrl VARCHAR(200),
    apiTransactionId VARCHAR(80),
    locationCountryCode VARCHAR(15),
    invoiceTypeIcon VARCHAR(100),
    vatCountryCode VARCHAR(5),
    exchangeRate DECIMAL(10,7) DEFAULT 1.0,
    paymentId VARCHAR(75),
    orderNo VARCHAR(50),
    orderNoExt VARCHAR(50),
    discountrate VARCHAR(50),
    isMatch BOOLEAN DEFAULT FALSE,
    paymentType VARCHAR(100) DEFAULT 'unknown',
    orderDate DATE,
    dueDate DATE,
    invoicePartyPhone VARCHAR(25),
    phone VARCHAR(50),
    deliveryDate DATE,
    deliveryCountryCode VARCHAR(5),
    additionalInfo VARCHAR(45),
    noticeConsultant VARCHAR(600),
    invoiceDueDate DATETIME,
    invoiceReferenceNo VARCHAR(45),
    documentDate DATE,
    statusApplication VARCHAR(20),
    attendant VARCHAR(80),
    paymentTypeId INT,
    subject VARCHAR(254),
    invoiceId INT,
    invoicePartyTaxId VARCHAR(45),
    invoicePartyBankName VARCHAR(60),
    invoicePartyBankAccountNo VARCHAR(50),
    invoicePartyBankIban VARCHAR(30),
    invoicePartyBankSwift VARCHAR(15),
    discountInvoiceDueDate DATE,
    nexusCountry VARCHAR(3) DEFAULT 'DEU',
    isB2b BOOLEAN DEFAULT FALSE
);
"""

table_invoiceListDetails = """
CREATE TABLE IF NOT EXISTS InvoiceListDetails (
    invoiceListId INT,
    inputChannel VARCHAR(45) NOT NULL,
    grossAmount DECIMAL(9,2) DEFAULT 0,
    exchangeRate DECIMAL(10,7) DEFAULT 1.0,
    netAmount DECIMAL(9,2) DEFAULT 0,
    vatAmount DECIMAL(9,2) DEFAULT 0,
    vatRate DECIMAL(9,2) DEFAULT 0,
    purchasePrice DECIMAL(9,2) DEFAULT 0,
    bookingText VARCHAR(500),
    participantBookingAccountNo VARCHAR(50),
    serialNumber VARCHAR(100),
    buCode INT,
    bookingAccountNo INT,
    cost INT,
    cost2 INT,
    artikel VARCHAR(250),
    invoiceNo VARCHAR(50),
    serialNumberId INT,
    sku VARCHAR(30),
    currency VARCHAR(5) DEFAULT 'EUR',
    isService BOOLEAN DEFAULT FALSE,
    isElectrService BOOLEAN DEFAULT FALSE,
    isDifferentialTax BOOLEAN DEFAULT FALSE,
    isDetailRateType BOOLEAN DEFAULT FALSE,
    accountingSuffix INT DEFAULT 0
);
"""

table_transactionList = """
CREATE TABLE IF NOT EXISTS TransactionList (
    transactionAccountId INT NOT NULL,
    clientId INT NOT NULL,
    date DATETIME NOT NULL,
    totalAmount DECIMAL(9,2) NOT NULL,
    csvImportId INT,
    partcipantName VARCHAR(100),
    outstandingAmount DECIMAL(9,2) DEFAULT 0,
    docNo INT,
    transactionAccount VARCHAR(45),
    transactionType VARCHAR(120),
    transactionPurpose TEXT,
    participantAccount VARCHAR(100),
    paricipantBlz VARCHAR(100),
    referenztransactionId VARCHAR(100),
    transactionParicipantNo VARCHAR(45),
    participantIban VARCHAR(45),
    paricipantBic VARCHAR(45),
    arrivalCountry VARCHAR(3),
    noticeConsultant VARCHAR(400),
    departCountry VARCHAR(3),
    accountIdentificationParticipant VARCHAR(140),
    referenztransactionIdTyp VARCHAR(100),
    transactionStatus VARCHAR(100),
    transactionNote VARCHAR(500),
    marketplace VARCHAR(100),
    isFinish BOOLEAN DEFAULT FALSE,
    clientTransactionNo INT DEFAULT 0,
    isExported BOOLEAN DEFAULT FALSE,
    currency VARCHAR(10) DEFAULT 'EUR',
    isCommit BOOLEAN DEFAULT FALSE,
    isPotentialDuplicate BOOLEAN DEFAULT FALSE,
    apiTransactionId VARCHAR(50),
    rgNumber VARCHAR(50),
    acountType VARCHAR(45),
    amazonSettlementId VARCHAR(75),
    valueDate DATETIME,
    participantEmail VARCHAR(250),
    attendant VARCHAR(80),
    statusApplication VARCHAR(20) DEFAULT 'offen',
    barcode VARCHAR(50),
    typeCodeZka VARCHAR(20),
    clientNo VARCHAR(75),
    customField VARCHAR(255),
    ifdStock DECIMAL(9,2),
    customField2 VARCHAR(50),
    isMatch BOOLEAN DEFAULT FALSE,
    exchangeRate DECIMAL(10,7) DEFAULT 0.0,
    dueDate DATE
);
"""

table_transactionListDetails = """
CREATE TABLE IF NOT EXISTS TransactionListDetails (
    transactionListId INT,
    artikel VARCHAR(500),
    trigerText VARCHAR(200),
    inputChannel VARCHAR(45),
    amount DECIMAL(9,2) NOT NULL,
    vatRate DECIMAL(9,2),
    isMatching BOOLEAN DEFAULT FALSE,
    exchangeRate DECIMAL(10,7) DEFAULT 1.0,
    isMatchRequired BOOLEAN DEFAULT TRUE,
    isMatchCompleted BOOLEAN DEFAULT FALSE,
    bookingText VARCHAR(250),
    buCode INT,
    cost INT,
    cost2 INT,
    participantBookingAccountNo INT,
    invoiceNo VARCHAR(45),
    currency VARCHAR(10) DEFAULT 'EUR',
    accountNo VARCHAR(80),
    fulfillmentId VARCHAR(50),
    departVatRate DECIMAL(9,2),
    accountingSuffix INT DEFAULT 0
);
"""

table_transactionSettlement = """
CREATE TABLE IF NOT EXISTS TransactionSettlement (
    settlementId VARCHAR(75) NOT NULL,
    transactionAccountId INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    settlementStartDate DATETIME,
    setlementEndDate DATETIME,
    currency VARCHAR(10) DEFAULT 'EUR',
    totalAmount DECIMAL(9,2) DEFAULT 0.0,
    startAmount DECIMAL(9,2) DEFAULT 0.0,
    endAmount DECIMAL(9,2) DEFAULT 0.0,
    depositDate DATETIME,
    ReportId VARCHAR(50),
    isCommit BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (settlementId, transactionAccountId, type)
);
"""

table_document = """
CREATE TABLE IF NOT EXISTS Document (
    isInvoice BOOLEAN DEFAULT TRUE,
    isVerify BOOLEAN DEFAULT FALSE,
    folderId INT NOT NULL,
    uploadedName VARCHAR(45) NOT NULL,
    name VARCHAR(250) NOT NULL,
    nameGuid VARCHAR(100) NOT NULL,
    inputChannel VARCHAR(45) NOT NULL,
    folder VARCHAR(45) NOT NULL,
    cc VARCHAR(45) NOT NULL,
    isOcr BOOLEAN DEFAULT FALSE,
    isAutoExport BOOLEAN DEFAULT FALSE,
    docMime VARCHAR(45) NOT NULL,
    docExtension VARCHAR(10) NOT NULL,
    isDatevDocType BOOLEAN DEFAULT FALSE,
    attendant VARCHAR(80) NOT NULL,
    statusApplication VARCHAR(20) DEFAULT 'offen',
    clientId INT NOT NULL,
    guid VARCHAR(100) NOT NULL,
    clientDocNo INT NOT NULL,
    creator VARCHAR(100) DEFAULT 'newsystemUser@digitastic.app'
);
"""

table_folder = """
CREATE TABLE IF NOT EXISTS Folder (
    id INT NOT NULL,
    clientId INT NOT NULL,
    name VARCHAR(45) NOT NULL,
    isOcr BOOLEAN DEFAULT FALSE,
    isAutoExport BOOLEAN DEFAULT FALSE,
    isDatevDocType BOOLEAN DEFAULT FALSE,
    defaultAttendant VARCHAR(80) NOT NULL,
    defaultStatus VARCHAR(15) DEFAULT 'offen',
    PRIMARY KEY (id)
);
"""

table_client = """
CREATE TABLE IF NOT EXISTS Client (
    cc VARCHAR(50) NOT NULL,
    PRIMARY KEY (cc)
);
"""

table_csvImportLog = """
CREATE TABLE IF NOT EXISTS CsvImportLog (
    description VARCHAR(275),
    totalCount INT DEFAULT 0,
    totalAmount DECIMAL(11,2) DEFAULT 0,
    errorMessage VARCHAR(250),
    startDate DATE,
    endDate DATE,
    lastWorkedDate DATETIME,
    isRunning BOOLEAN DEFAULT FALSE
);
"""

table_clientAccountBookingRules = """
CREATE TABLE IF NOT EXISTS ClientAccountBookingRules (
    transactionAccountId INT,
    invoiceAccountId INT,
    triggerText VARCHAR(200),
    buCode INT,
    cost INT,
    cost2 INT,
    isInvoice BOOLEAN DEFAULT FALSE,
    isMatchingPayment BOOLEAN DEFAULT FALSE,
    bookingAccount VARCHAR(25)
);
"""

table_defaultBookingRules = """
CREATE TABLE IF NOT EXISTS DefaultBookingRules (
    glfrmtyp VARCHAR(200),
    triggerText VARCHAR(200),
    bookingAccount VARCHAR(25),
    bookingRulesGroupId INT
);
"""

table_transactionInvoiceList = """
CREATE TABLE IF NOT EXISTS TransactionInvoiceList (
    clientId INT NOT NULL,
    transactionId INT NOT NULL,
    transactionDetailId INT NOT NULL,
    invoiceId INT,
    isAutoMatching BOOLEAN DEFAULT FALSE,
    isInvoice BOOLEAN DEFAULT TRUE,
    isTransaction BOOLEAN DEFAULT TRUE,
    guid VARCHAR(60),
    name VARCHAR(60)
);
"""

table_invoiceTagsList = """
CREATE TABLE IF NOT EXISTS InvoiceTagsList (
    clientId INT NOT NULL,
    tag VARCHAR(50) NOT NULL,
    documentIId INT
);
"""

table_accountErrorStatusCode = """
CREATE TABLE IF NOT EXISTS clientPortalErrStatusCode (
    errStatusCode INT NOT NULL,
    statement VARCHAR(35) NOT NULL,
    PRIMARY KEY (errStatusCode)
);
"""

table_portalStatusCode = """
CREATE TABLE IF NOT EXISTS portalStatusCode (
    statusCode INT NOT NULL,
    statement VARCHAR(50) NOT NULL,
    PRIMARY KEY (statusCode)
);
"""

# Kullanım örneği:

CREATE_TABLES = [
    table_invoiceList,
    table_invoiceListDetails,
    table_transactionList,
    table_transactionListDetails,
    table_transactionSettlement,
    table_document,
    table_folder,
    table_client,
    table_csvImportLog,
    table_clientAccountBookingRules,
    table_defaultBookingRules,
    table_transactionInvoiceList,
    table_invoiceTagsList,
    table_accountErrorStatusCode,
    table_portalStatusCode,
]

def create_all_tables():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            for table_sql in CREATE_TABLES:
                cur.execute(table_sql)
        conn.commit()
        print("Tüm tablolar başarıyla oluşturuldu.")
    except Exception as e:
        print(f"Tablo oluşturulurken hata oluştu: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_all_tables()
