-- AlterTable
ALTER TABLE `Effect` ADD COLUMN `conditions` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `Item` ADD COLUMN `conditions` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `Skill` ADD COLUMN `conditions` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `Trait` ADD COLUMN `conditions` VARCHAR(191) NULL;
