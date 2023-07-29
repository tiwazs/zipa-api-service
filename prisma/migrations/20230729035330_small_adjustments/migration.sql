-- AlterTable
ALTER TABLE `Effect` ADD COLUMN `vitality_recovery` VARCHAR(191) NULL,
    MODIFY `max_stack` INTEGER NULL;

-- AlterTable
ALTER TABLE `Item` ADD COLUMN `vitality_recovery` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `Skill` ADD COLUMN `vitality_recovery` VARCHAR(191) NULL,
    MODIFY `cooldown` DOUBLE NOT NULL DEFAULT 0,
    MODIFY `channeled` BOOLEAN NOT NULL DEFAULT false;
