from adminOperations.constants import BULK_IMPORT_COLS, BULK_IMPORT_VERSIONS, BULK_IMPORT_ERROR_SCHEMA, \
    BULK_IMPORT_ERROR_CODES, BULK_IMPORT_MANDATORY_FIELDS


class ExcelValidations():

    def __init__(self):
        self.validation_result = {}
        self.work_sheet_data_list = list()
        self.headers = list()

    def validate_uploaded_sheet(self,work_sheet):
        for column_index in xrange(work_sheet.ncols):
            col_header = work_sheet.cell(0, column_index).value
            self.headers.append(col_header.upper())
        self.header_validation(self.headers)
        self.data_validation(work_sheet)
        return self.validation_result

    def header_validation(self, headers):
        latest_sheet_template = BULK_IMPORT_COLS.get(BULK_IMPORT_VERSIONS[-1])
        for each_header in latest_sheet_template.keys():
            if each_header not in headers:
                self.validation_result["result"] = {"errorCode":BULK_IMPORT_ERROR_SCHEMA.get("HEADER MISMATCH"),
                                                    "errorMsg":BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("HEADER MISMATCH"))
                                                    }

    def data_validation(self, work_sheet):
        for row_index in xrange(1, work_sheet.nrows):
            row_dict = {self.headers[col_index]:work_sheet.cell(row_index,col_index).value for col_index in xrange(work_sheet.ncols)}
            self.work_sheet_data_list.append(row_dict)
        for each_data_row in self.work_sheet_data_list:
            for key, value in each_data_row.items():
                if not value and key in BULK_IMPORT_MANDATORY_FIELDS:
                    self.validation_result["result"] = {"errorCode":BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING"),
                                                        "errorMsg":BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING")).format(key)
                                                        }
    def getValidatedProjectsList(self, work_sheet):
        projects_list = list()
        for column_index in xrange(work_sheet.ncols):
            col_header = work_sheet.cell(0, column_index).value
            self.headers.append(col_header.upper())
        for row_index in xrange(1, work_sheet.nrows):
            row_dict = {self.headers[col_index]:work_sheet.cell(row_index,col_index).value for col_index in xrange(work_sheet.ncols)}
            projects_list.append(row_dict)
        return projects_list


