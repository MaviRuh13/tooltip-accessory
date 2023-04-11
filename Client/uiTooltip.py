# Arat - Search:
	def __AppendAccessoryMetinSlotInfo(self, metinSlot, mtrlVnum):		
		ACCESSORY_SOCKET_MAX_SIZE = 3		

		cur=min(metinSlot[0], ACCESSORY_SOCKET_MAX_SIZE)
		end=min(metinSlot[1], ACCESSORY_SOCKET_MAX_SIZE)

		affectType1, affectValue1 = item.GetAffect(0)
		affectList1=[0, max(1, affectValue1*10/100), max(2, affectValue1*20/100), max(3, affectValue1*40/100)]

		affectType2, affectValue2 = item.GetAffect(1)
		affectList2=[0, max(1, affectValue2*10/100), max(2, affectValue2*20/100), max(3, affectValue2*40/100)]

		mtrlPos=0
		mtrlList=[mtrlVnum]*cur+[player.METIN_SOCKET_TYPE_SILVER]*(end-cur)
		for mtrl in mtrlList:
			affectString1 = self.__GetAffectString(affectType1, affectList1[mtrlPos+1]-affectList1[mtrlPos])			
			affectString2 = self.__GetAffectString(affectType2, affectList2[mtrlPos+1]-affectList2[mtrlPos])

			leftTime = 0
			if cur == mtrlPos+1:
				leftTime=metinSlot[2]

			self.__AppendMetinSlotInfo_AppendMetinSocketData(mtrlPos, mtrl, affectString1, affectString2, leftTime)
			mtrlPos+=1

# Deðiþtir - Change:
	def __AppendAccessoryMetinSlotInfo(self, metinSlot, mtrlVnum):
		ACCESSORY_SOCKET_MAX_SIZE = 3

		cur=min(metinSlot[0], ACCESSORY_SOCKET_MAX_SIZE)
		end=min(metinSlot[1], ACCESSORY_SOCKET_MAX_SIZE)

		
		affectType1, affectValue1 = item.GetAffect(0)
		affectType2, affectValue2 = item.GetAffect(1)
		affectType3, affectValue3 = item.GetAffect(2)

		mtrlPos=0
		mtrlList=[mtrlVnum]*cur+[player.METIN_SOCKET_TYPE_SILVER]*(end-cur)
		
		if app.ENABLE_TOOLTIP_ACCESSORY:
			attr_total = [0,0,0,0,0]
			self.AppendSpace(5)
			if mtrlVnum > 0 and end > 0:
				item.SelectItem(mtrlVnum)
				self.AppendTextLine(str(item.GetItemName()),self.CONDITION_COLOR)
				self.AppendSpace(5)
				
			socket_lv = metinSlot[2]
			sockets=[]
			i = 0
				
			while(socket_lv > 0):
				mod = int(socket_lv % 10)
				sockets.append(int(mod))
				socket_lv = int(socket_lv / 10)
				i+=1
			
			sockets.reverse()
			
			#self.AppendTextLine("[{}]".format(','.join([str(i) for i in sockets])), 0xFF00b6d6)
			
			height = self.toolTipHeight
		
		for mtrl in mtrlList:
			if app.ENABLE_TOOLTIP_ACCESSORY:
				lv = 0
				if mtrl > 1:
					lv = sockets[mtrlPos]
					
				
				newP = 175
				affectList1=[0, max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP)), max(1, affectValue1*(5*lv)/int(newP))]
				affectList2=[0, max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP)), max(1, affectValue2*(5*lv)/int(newP))]
				affectList3=[0, max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP)), max(1, affectValue3*(5*lv)/int(newP))]
			

				affectString1 = self.__GetAffectString(affectType1, affectList1[mtrlPos+1])
				affectString2 = self.__GetAffectString(affectType2, affectList2[mtrlPos+1])
				affectString3 = self.__GetAffectString(affectType3, affectList3[mtrlPos+1])
				if mtrl > 1:
					if affectString1:
						attr_total[0] += affectList1[mtrlPos+1]
						
					if affectString2:
						attr_total[1] += affectList2[mtrlPos+1]
						
					if affectString3:
						attr_total[2] += affectList3[mtrlPos+1]
			else:
				affectString1 = self.__GetAffectString(affectType1, affectList1[mtrlPos+1]-affectList1[mtrlPos])
				affectString2 = self.__GetAffectString(affectType2, affectList2[mtrlPos+1]-affectList2[mtrlPos])
				affectString3 = self.__GetAffectString(affectType3, affectList3[mtrlPos+1]-affectList3[mtrlPos])

			leftTime = 0
			if cur == mtrlPos+1:
				leftTime=metinSlot[2]

			
			
			if app.ENABLE_TOOLTIP_ACCESSORY:
				self.__AppendMetinSlotInfo_AppendMetinSocketData_New(mtrlPos, mtrl, height, end, lv)
			else:
				self.__AppendMetinSlotInfo_AppendMetinSocketData(mtrlPos, mtrl, affectString1, affectString2, affectString3, leftTime)
			mtrlPos+=1
			
		if app.ENABLE_TOOLTIP_ACCESSORY:
			if end > 0:
				if end > 4:
					self.toolTipHeight += 70
				else:
					self.toolTipHeight += 35
				
				self.ResizeToolTip()
			
				affectString11 = self.__GetAffectString(affectType1, attr_total[0])			
				affectString22 = self.__GetAffectString(affectType2, attr_total[1])
				affectString33 = self.__GetAffectString(affectType3, attr_total[2])
				
				
				self.AppendSpace(5)
				if affectString11:
					self.AppendTextLine(affectString11, self.POSITIVE_COLOR)
				if affectString22:
					self.AppendTextLine(affectString22, self.POSITIVE_COLOR)
				if affectString33:
					self.AppendTextLine(affectString33, self.POSITIVE_COLOR)

				
			self.ResizeToolTip()

	if app.ENABLE_TOOLTIP_ACCESSORY:
		def __AppendMetinSlotInfo_AppendMetinSocketData_New(self, index, metinSlotData, height=0, end=0, socket_lv=0):
			slotType = self.GetMetinSocketType(metinSlotData)
			itemIndex = self.GetMetinItemIndex(metinSlotData)
			
			if 0 == slotType:
				return

			slotImage = ui.ImageBox()
			slotImage.SetParent(self)
			slotImage.Show()

			

			if player.METIN_SOCKET_TYPE_SILVER == slotType:
				slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_silver.sub")
			elif player.METIN_SOCKET_TYPE_GOLD == slotType:
				slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_gold.sub")

			self.childrenList.append(slotImage)
		
				
			if index > 3:
				height += 35
				index = index-4
				
			if end > 4:
				end = 4
			
			calc_x = (self.toolTipWidth/2) - (17.5*end)
			
			slotImage.SetPosition(calc_x+index*35, height)

			metinImage = ui.ImageBox()
			metinImage.SetParent(slotImage)
			metinImage.Show()
			self.childrenList.append(metinImage)
			
			lvText = ui.TextLine()
			lvText.SetParent(metinImage)
			lvText.SetFontName(self.defFontName)
			lvText.SetPackedFontColor(self.CONDITION_COLOR)
			lvText.SetOutline()
			lvText.SetFeather()
			# lvText.Show()
			lvText.Hide()

			self.childrenList.append(lvText)

			if itemIndex:
				item.SelectItem(itemIndex)

				## Image
				try:
					metinImage.LoadImage(item.GetIconImageFileName())
				except:
					dbg.TraceError("ItemToolTip.__AppendMetinSocketData() - Failed to find image file %d:%s" % 
						(itemIndex, item.GetIconImageFileName())
					)

				metinImage.SetPosition(1, 1)
				lvText.SetPosition(6, 16)
				lvText.SetText("Lv %d" % (socket_lv))
