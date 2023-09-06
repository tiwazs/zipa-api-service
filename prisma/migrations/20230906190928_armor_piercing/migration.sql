-- AlterTable
ALTER TABLE `Effect` ADD COLUMN `armor_piercing` VARCHAR(191) NULL,
    ADD COLUMN `spell_piercing` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `Item` ADD COLUMN `armor_piercing` VARCHAR(191) NULL,
    ADD COLUMN `spell_piercing` VARCHAR(191) NULL;
