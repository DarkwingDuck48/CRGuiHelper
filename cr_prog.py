# <-- codind: utf-8 -->
'''
author: Maxim Britvin
email: maksbritvin@gmail.com
TODO:
1. Check all actual files versions
2. Do optional settings
3. Write OOP
'''

import os
import sys
import json
import os.path
import shutil


class NewCR:
    def __init__(self):
        self.templateDir = os.path.abspath(os.getenv('USERPROFILE') + '\\Documents\\Templates')
        self.workDir = os.path.abspath(os.getenv('USERPROFILE') + '\\Documents\\CRs')
        self.allDir = os.listdir(self.workDir)
        self.options = []
        self.aviableself = False

    def createnewcr(self):
        self.crNumb = input("Print number of your CR: ")

        while not self.aviableself:  # Validation check of CR's name
            if not self.crNumb.isnumeric():
                print('Enter number of your CR!')
                self.crNumb = input("Print number of your CR: ")
            else:
                self.crName = 'CR-' + self.crNumb
                if self.crName not in self.allDir:
                    self.aviableself = True
                elif self.crName in self.allDir:
                    print('This CR has already been in directory')
                    self.crName = "CR-" + input('Print name of your CR: ')
        print('Valid name.')
        self.crDir = self.workDir + '\\' + self.crName
        self.createDir()
        self.templatecreate()
        self.option()

    # Options of creation CR documentation
    def option(self):
        question = input('Copy HPL delivery? Yes/No ')  # Making HPL_delivery_template
        while question.lower() not in ['yes', 'y', 'no', 'n']:
            print('Please, chose Yes or No')
            question = input('Copy HPL delivery? Yes/No ')
        if self.yesno(question):
            shutil.copyfile(self.templateDir + '\\Actual Files\\HPL_delivery format_v3.19.xls',
                            self.crDir + '\\HPL_delivery_template.xls')
            if os.path.isfile(self.crDir + '\\HPL_delivery_template.xls'):
                print('Created HPL_delivery_template.xls')
        question = input('Create {} toolkit? Yes/No '.format(self.crName))  # Making Toolkit
        while question.lower() not in ['yes', 'y', 'no', 'n']:
            print('Please, chose Yes or No')
            question = input('Create {} toolkit? Yes/No '.format(self.crName))
        if self.yesno(question):
            shutil.copyfile(self.templateDir + '\\startCR\\CR Toolkit.xlsx',
                            self.crDir + '\\' + self.crName + ' Toolkit.xlsx')
            if os.path.isfile(self.crDir + '\\' + self.crName + ' Toolkit.xlsx'):
                print('Created {} Toolkit.xlsx'.format(self.crName))
        question = input('Do you change metadata in {}? Yes/No '.format(self.crName))  # Copy actual metadata
        while question.lower() not in ['yes', 'y', 'no', 'n']:
            print('Please, chose Yes or No')
            question = input('Do you change metadata in {}? Yes/No '.format(self.crName))
        if self.yesno(question):
            shutil.copyfile(self.templateDir + '\\Actual Files\\GRSHFM_Metadata_v16110102.xlsb',
                            self.crDir + '\\GRSHFM_Metadata_v16110102.xlsb')
            if os.path.isfile(self.crDir + '\\GRSHFM_Metadata_v16110102.xlsb'):
                print('Created metadata.')

    def applyoptions(self, options):
        pass

    def createDir(self):  # Func to create new directory for CR
        print('Making folder for %s...' % self.crName)
        os.mkdir(self.workDir + '\\' + self.crName)
        if os.path.isdir(self.workDir + '\\' + self.crName):
            print('Done.')

    def templatecreate(self):  # Funct to create start templates(TD,FD,TE) for CR
        print('Prepare to create templates...')
        shutil.copyfile(self.templateDir + '\\startCR\\TE_v1.00.docx',
                        self.workDir + '\\' + self.crName + '\\' + 'TE_CR_' + self.crName[-2:] + '_v1.00.docx')
        if os.path.isfile(self.workDir + '\\' + self.crName + '\\' + 'TE_CR_' + self.crName[-2:] + '_v1.00.docx'):
            print('Created TE_CR_{}_v1.00.docx'.format(self.crName[-2:]))
        shutil.copyfile(self.templateDir + '\\startCR\\FD_v1.00.docx',
                        self.workDir + '\\' + self.crName + '\\' + 'FD_CR_' + self.crName[-2:] + '_v1.00.docx')
        if os.path.isfile(self.workDir + '\\' + self.crName + '\\' + 'FD_CR_' + self.crName[-2:] + '_v1.00.docx'):
            print('Created FD_CR_{}_v1.00.docx'.format(self.crName[-2:]))
        shutil.copyfile(self.templateDir + '\\startCR\\TD_v1.00.docx',
                        self.workDir + '\\' + self.crName + '\\' + 'TD_CR_' + self.crName[-2:] + '_v1.00.docx')
        if os.path.isfile(self.workDir + '\\' + self.crName + '\\' + 'TD_CR_' + self.crName[-2:] + '_v1.00.docx'):
            print('Created TD_CR_{}_v1.00.docx'.format(self.crName[-2:]))

    def yesno(self, question):
        if question.lower() == 'yes':
            return True
        elif question.lower == 'no':
            return False


if __name__ == '__main__':

    # Read and check settings for programm enviroment

    with open('config.json', 'r', encoding='utf-8') as fh:
        config = json.load(fh)
    if config['userlogin'] == os.getlogin():
        print('Settings are set for current user')
    if config['userlogin'] != os.getlogin() or config['userlogin'] == "":
        print('New user')
        config['userlogin'] = os.getlogin()
        question = input('Do you want to use default folder for your CR\'s? \nIt will be {}: '.format(
            os.path.abspath(os.getenv('USERPROFILE') + '\\Documents\\CRs')))
        with open('config.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(config, ensure_ascii=False, sort_keys=True, indent=4))

    '''
	print ('Hello,{}!'.format(os.getlogin()))
	programmstart = True
	w = NewCR()
	def intra():
		print('If you want to start programm, write 1')
		print('If you want to change config, write 2')
		print('If you want to exit, write 0')
		action = int(input('Write your number here: '))
		if action not in [1,2,0]:
			while action not in [1,2,0]:
				print("Invalid chose. Please type 1,2 or 0")
				action = int(input('Write your number here: '))
		return action
	while programmstart == True:
		action = intra()
		if action == 1:
			w.createnewcr()
		elif action == 2:
			print("tadada ta ta")
		if action == 0:
			print ('Exit programm.')
			programmstart = False
			try:
				sys.exit()
			except SystemExit:
				print ('Goodbye,{}!'.format(os.getlogin()))
	'''
