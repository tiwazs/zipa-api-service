-- AlterTable
ALTER TABLE `Unit` ADD COLUMN `ascended` BOOLEAN NOT NULL DEFAULT false,
    ADD COLUMN `ascended_params` VARCHAR(191) NULL;
